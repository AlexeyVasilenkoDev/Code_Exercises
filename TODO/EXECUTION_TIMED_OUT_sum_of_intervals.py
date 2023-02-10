# def sum_of_intervals(intervals):
#     numbers_list = []
#     for i in intervals:
#         for y in range(i[0], i[1]):
#             numbers_list.append(y)
#     return len(set(numbers_list))
link = "https://www.codewars.com/kata/52b7ed099cdc285c300001cd"


def sum_of_intervals(intervals):
    numbers_list = set(y for i in intervals for y in range(i[0], i[1]))
    return len(set(numbers_list))


print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
