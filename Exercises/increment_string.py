link = "https://www.codewars.com/kata/54a91a4883a7de5d7800009c/"


def increment_string(strng):
    numbers = []
    for i in strng[::-1]:
        if i.isdigit():
            numbers.append(i)
        elif i.isdigit() is False:
            break
    if len(numbers) > 0:
        strng = strng[:(len(strng) - len(numbers))]
        for _ in range(len(numbers) - len(str(int(''.join(numbers[::-1])) + 1))):
            strng += '0'
        return strng + str(int(''.join(numbers[::-1])) + 1)
    return strng + '1'
