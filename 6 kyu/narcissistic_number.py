link = "https://www.codewars.com/kata/5287e858c6b5a9678200083c"


def narcissistic(value):
    values_list = [int(i) for i in str(value)]
    return value == sum(list(map(lambda x: x ** len(str(value)), values_list)))


print(narcissistic(371))
