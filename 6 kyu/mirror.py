link = "https://www.codewars.com/kata/581331293788bc1702001fa6"


def mirror(text):
    reverse_words = [i[::-1] for i in text.split()]
    mirror_width = len(max(reverse_words, key=len)) + 4
    word = '*' * mirror_width + "\n"
    for i in reverse_words:
        word += "*" + " " + i + " " * (mirror_width - len(i) - 3) + "*" + "\n"
    return word + '*' * mirror_width


print(mirror("Hello World"))