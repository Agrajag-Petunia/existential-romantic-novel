def extract_project_gutenberg_novel(text):
    start = "START OF THIS PROJECT GUTENBERG"
    end = "END OF THIS PROJECT GUTENBERG"
    return find_between(text, start, end)


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def remove_titles(text):
    lines = []
    for line in text.split('\n'):
        if (not line.isupper() and 'chapter' not in line.lower()
                and 'produced by' not in line.lower()):
            lines.append(line)

    return '\n'.join(lines)


def valid_word(word):
    result = False
    if '\n\n\n' not in word:
        for c in word:
            if c.isdigit():
                break
        else:
            result = True

    return result
