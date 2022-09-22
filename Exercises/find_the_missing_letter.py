import string

link = "https://www.codewars.com/kata/5839edaa6754d6fec10000a2"


def find_missing_letter(chars):
    letters = string.ascii_letters
    range_of_letters = letters[letters.index(chars[0]):letters.index(chars[-1]) + 1]
    missing_letter = [i for i in range_of_letters if i not in chars]
    return missing_letter[0]


print(find_missing_letter(["a", "b", "c", "d", "f"]))
