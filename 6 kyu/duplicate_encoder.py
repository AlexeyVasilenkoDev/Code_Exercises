link = "https://www.codewars.com/kata/54b42f9314d9229fd6000d9c"


def duplicate_encode(word):
    char_counter = {}
    result = ''
    for i in word:
        if i.lower() in char_counter.keys():
            char_counter[i.lower()] += 1
        else:
            char_counter[i.lower()] = 1
    for y in word:
        if char_counter[y.lower()] > 1:
            result += ')'
        else:
            result += '('
    return result


print(duplicate_encode('din'))
print(duplicate_encode('recede'))
print(duplicate_encode('Success'))
print(duplicate_encode('(( @'))
print(duplicate_encode('CodeWarrior'))
