link = "https://www.codewars.com/kata/52597aa56021e91c93000cb0/"


def move_zeros(lst: list):
    number_of_zeros = lst.count(0)
    return [i for i in lst if i != 0] + [0] * number_of_zeros


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
