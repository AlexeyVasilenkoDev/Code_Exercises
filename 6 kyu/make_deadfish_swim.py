link = "https://www.codewars.com/kata/51e0007c1f9378fa810002a9"


def parse(data):
    result = []
    i = 0
    commands = {
        'i': + 1,
        'd': - 1,
    }
    for k in data:
        if k == 's':
            i = i ** 2
        elif k == 'o':
            result.append(i)
        elif k == 'i' or k =='d':
            i += commands[k]
        else:
            continue
    return result
