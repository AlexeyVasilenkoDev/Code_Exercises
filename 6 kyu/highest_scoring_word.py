import string

link = "https://www.codewars.com/kata/57eb8fcdf670e99d9b000272"


def high(x):
    list_of_sums = []
    words = x.split(' ')
    for word in words:
        sum = 0
        for i in word.lower():
            sum += string.ascii_lowercase.index(i) + 1
        list_of_sums.append(sum)
    return words[list_of_sums.index(max(list_of_sums))]
