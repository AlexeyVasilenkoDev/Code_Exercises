link = "https://www.codewars.com/kata/52742f58faf5485cae000b9a"


def format_duration(seconds):
    translated_seconds = {
        'years': 31536000,
        'days': 86400,
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }
    result = []
    if seconds == 0:
        return 'now'
    while seconds >= 1:
        for k, v in translated_seconds.items():
            if seconds / v >= 1:
                if int(seconds / v) == 1:
                    result += [str(int(seconds / v)), k[:-1]]
                else:
                    result += [str(int(seconds / v)), k]
                seconds -= int(seconds / v) * v
        break

    it = iter(result)
    new_result = [i[0] + ' ' + i[1] for i in list(zip(it, it))]
    if len(new_result) > 1:
        new_result.insert(-1, 'and')
    return ', '.join(new_result).replace(', and,', ' and')


print(format_duration(360))
print(format_duration(3660))
print(format_duration(3856))
print(format_duration(89520))
print(format_duration(3662))
