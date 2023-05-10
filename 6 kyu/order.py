link = "https://www.codewars.com/kata/55c45be3b2079eccff00010f"


def order(sentence):
    result = sentence.split()
    res_dict = dict()
    for i in result:
        for j in i:
            if j.isdigit():
                res_dict[int(j)] = i
    return list(map(lambda y: y[1], sorted(res_dict.items(), key=lambda x: x[0])))


print(order("is2 Thi1s T4est 3a"))
