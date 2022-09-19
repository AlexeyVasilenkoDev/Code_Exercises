# 30 хвилин
#
#
# def find_lake_depth(relief: list) -> int:
#     if len(set(relief)) == 1 or sorted(relief) == relief or sorted(relief) == relief[::-1]:
#         return 0
#     else:
#         depth_list = []
#         for index, elem in enumerate(relief):
#             try:
#                 if relief[index] > relief[index+1]:
#                     depth_list.append([relief[index], relief[index+1]])
#             except IndexError:
#                 break
#         for index, elem in enumerate(depth_list):
#             while depth_list[index][0] > depth_list[index+1][0]:
#                 try:
#                     if depth_list[index][0] > depth_list[index+1][0]:
#                         depth_list[index] = [depth_list[index][0], depth_list[index+1][1]]
#                         depth_list.remove(depth_list[index+1])
#                 except IndexError:
#                     print('A')
#         print(depth_list)
#
#
# print(find_lake_depth([1, 2, 3, 4, 5, 6, 7]))
# print(find_lake_depth([100, 0, 100]))
# print(find_lake_depth([6, 5, 4]))
# print(find_lake_depth([1, 1, 1, 1]))
# print(find_lake_depth([1, 10, 3, 7, 0, 23]))
# print(find_lake_depth([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]))
# print(find_lake_depth([1, 2, 5, 6, 1, 2, 2, 3, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]))


def find_lake_depth(relief: list) -> int:
    left_peak = 0
    fall = 0
    depth = 0
    for i in range(len(relief)):
        if i > 0:
            if relief[i] < relief[i - 1]:
                fall = relief[i]
                if relief[i - 1] > left_peak:
                    left_peak = relief[i - 1]
            elif relief[i] < fall:
                fall = relief[i]
            elif relief[i] > fall:
                max_right_peak = relief[i]
                new_depth = min(left_peak, max_right_peak) - fall
                if new_depth > depth:
                    depth = new_depth
    return depth


if __name__ == "__main__":
    assert (find_lake_depth([1, 2, 3, 4, 5, 6, 7]) == 0)
    assert (find_lake_depth([100, 0, 100]) == 100)
    assert (find_lake_depth([6, 5, 4]) == 0)
    assert (find_lake_depth([1, 1, 1, 1]) == 0)
    assert (find_lake_depth([1, 10, 3, 7, 0, 23, 2, 5, 11]) == 10)
    assert (find_lake_depth([1, 2, 5, 7, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 7)
    assert (find_lake_depth([1, 2, 5, 6, 1, 2, 2, 3, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
    assert (find_lake_depth([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
    assert (find_lake_depth([9, 0, 9, 12, 2, 12]) == 10)
    assert (find_lake_depth([1, 1, 9, 12, 18, 12]) == 0)
    assert (find_lake_depth([1, 1, 9, 12, 9, 12]) == 3)
    assert (find_lake_depth([1, 1]) == 0)
    print('Done!')
