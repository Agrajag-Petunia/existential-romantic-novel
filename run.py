from datetime import datetime

from src.textgenerator import TextGenerator
from src.utils import extract_project_gutenberg_novel, remove_titles

# The source files to use
# NOTE: Ulysses makes the generated text just a little too weird.
files = [
    './data/life_and_amours.txt',
    './data/memoirs_of_fanny_hill.txt',
    './data/metamorphosis.txt',
    './data/the_romance_of_lust.txt',
    './data/the_trial.txt',
    # './data/ulysses.txt',
    './data/the_antichrist.txt',
    './data/beyond_good_and_evil.txt',
]

total_word_count = 50000
chapters = 23
words_per_chapter = int(50000 / 23)

output = ""

# Build our text generator (I found a prefix length of 2 or 3 worked best)
model = TextGenerator(prefix_length=3)

# Just to remind you which novels are being used
print(files)

# Iterate over our files
for filename in files:
    # For each file read in the text and work it into our
    # model.
    with open(filename, 'r') as fobj:
        print('Learning text from {}...'.format(filename))
        # remove project gutenberg license stuff from the text
        text = extract_project_gutenberg_novel(fobj.read())
        # Strip the title, chapters, etc from the text.
        text = remove_titles(text)
        # Learn the cleaned up text
        model.learn(text)


# Start generating our novel
with open('./data/novel.txt', 'w') as fobj:
    # Start by printing out summary content
    fobj.write("You are free and that is why you lust\n")
    fobj.write("=====================================\n\n")
    fobj.write("Author: Agrajag Petunia's computer\n")
    fobj.write("Generation Date: {}\n\n".format(
        datetime.now().strftime("%Y-%m-%d")
    ))

    # For each chapter generate some text
    for c in range(1, chapters + 1):
        fobj.write("\n\n\tChapter {}\n".format(c))
        fobj.write("---------------------------\n")
        output = model.generate(size=words_per_chapter)
        fobj.write(output)
