import random
import re

from .utils import valid_word


class TextGenerator(object):
    """
    Pretty simple text generator using
    a Markov Chain. The code for this class is
    based off of the following gist.

    https://gist.github.com/agiliq/131679#file-gistfile1-py
    """
    def __init__(self, prefix_length=2):
        """
        The TextGenerator needs to maintain
        a prefix table, prefix_length and a list of
        words.
        """
        self.prefix_table = {}
        self.prefix_length = prefix_length
        self.words = []

    def learn(self, text):
        """
        For lack of a better name learn parses the provided
        text using a sliding window over the words and adds them
        to the prefix_table. Since, learn can be called multiple times
        we append the words in the text provided to the list of words
        stored in the Generator.
        """
        words = []
        paragraphs = text.split('\n\n')
        for paragraph in paragraphs:
            for w in paragraph.split():
                if valid_word(w):
                    words.append(w)

            words.append('\n\n')

        self.words.extend(words)

        if len(words) < self.prefix_length + 1:
            return

        for i in range(len(words) - self.prefix_length):
            window = tuple(words[i + j] for j in range(self.prefix_length + 1))
            key = window[0:-1]
            val = window[-1]

            if key in self.prefix_table:
                self.prefix_table[key].append(val)
            else:
                self.prefix_table[key] = [val]

    def generate(self, size=100):
        """
        Rather than requiring some input text we randomly
        select the tuple to start with and them randomly
        select the suffix using random.choice from the
        prefix_table.
        """
        words = []
        key = self._seed()

        i = 0
        while i < size or not key[1].endswith('.'):
            # print('{} : {}'.format(key, (key in self.prefix_table)))

            words.append(key[0])
            if key not in self.prefix_table:
                key = self._seed()

            choice = random.choice(self.prefix_table[key])

            shifted = [key[j] for j in range(1, self.prefix_length)]
            shifted.append(choice)
            key = tuple(shifted)
            i += 1

        words.append(key[1])
        text = ' '.join(words)
        text = re.sub(' \n', '\n', text)
        return re.sub('\n\n\n+', '\n\n', text)

    def _seed(self):
        key = ()

        while True:
            seed = random.randint(
                0,
                (len(self.words) - (self.prefix_length + 1))
            )

            if self.words[seed][0].isupper():
                key = tuple(self.words[seed + i] for i in range(self.prefix_length))
                break

        return key
