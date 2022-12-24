# link = https://leetcode.com/problems/happy-number/description/

def isHappy(n: int):
    result = n
    res_list = []
    while result != 1:
        result = sum(list(map(lambda x: x**2, [int(i) for i in str(result)])))
        res_list.append(result)
        if 4 in res_list:
            return False
    return True


print(isHappy(19))
print(isHappy(2))
