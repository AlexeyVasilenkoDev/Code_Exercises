link = "https://www.codewars.com/kata/5526fc09a1bbd946250002dc/"


def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x % 2 == 1]
    return evens[0] if len(evens) == 1 else odds[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
