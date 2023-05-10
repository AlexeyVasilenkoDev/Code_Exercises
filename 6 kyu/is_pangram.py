link = "https://www.codewars.com/kata/545cedaa9943f7fe7b000048"


def is_pangram(s):
    pangram = set()
    for i in s.lower():
        if i.isalpha():
            pangram.add(i)
    if len(pangram) == 26:
        return True
    return False
