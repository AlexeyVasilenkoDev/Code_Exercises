import itertools

link = "https://www.codewars.com/kata/55983863da40caa2c900004e/train/python"


def next_bigger(n):
    list_of_digits = list(str(n))
    raw_result = []
    for digit in itertools.permutations(list_of_digits, len(list_of_digits)):
        if ''.join(digit) not in raw_result:
            raw_result.append(''.join(digit))
    result = sorted(raw_result)
    if result.index(str(n)) != len(result)-1:
        return int(result[result.index(str(n)) + 1])
    return -1


print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
print(next_bigger(1943947))
print(next_bigger(5225))
print(next_bigger(3254543))
