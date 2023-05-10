link = "https://www.codewars.com/kata/54e6533c92449cc251001667"


def unique_in_order(seq: str | list):
    if seq:
        result = [seq[0]]
        cur = seq[0]
        for i in seq:
            if cur == i:
                pass
            else:
                result.append(i)
            cur = i
        return result
    return []


print(unique_in_order(["a", "b", "b", "a"]))
print(unique_in_order([1, 2, 3, 3, -1]))
