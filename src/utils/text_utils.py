import unicodedata

def align_text(text, width):
    """
    按显示宽度补空格（支持中文）
    """

    current = 0

    for c in text:
        if unicodedata.east_asian_width(c) in ("F", "W"):
            current += 2
        else:
            current += 1

    return text + " " * (width - current)


def display_width(text):
    width = 0

    for c in text:
        if unicodedata.east_asian_width(c) in ("F", "W"):
            width += 2
        else:
            width += 1

    return width