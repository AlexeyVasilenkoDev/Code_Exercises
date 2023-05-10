def is_odd_heavy(arr):
    odds = []
    evens = []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if not odds:
        return False
    for j in evens:
        for k in odds:
            if j > k:
                return False
    return True
    # return biggest_int % 2 == 1


print(is_odd_heavy([]))
print(is_odd_heavy([11, 4, 9, 2, 3, 10]))
print(is_odd_heavy([11, 4, 9, 2, 8]))
print(is_odd_heavy([0, 0, 0]))
