def score(dice):
    result = 0
    dice_results = dict()
    for i in dice:
        if i not in dice_results:
            dice_results[i] = 1
        else:
            dice_results[i] += 1

    for k, v in dice_results.items():
        if v >= 3 and k != 1:
            result += k * 100
            if k == 5:
                v -= 3
        elif k == 1 or k == 5:
            while v > 0:
                if v >= 3:
                    if k == 1:
                        result += k * 1000
                        v -= 3
                else:
                    if k == 5:
                        result += k * 10 * v
                        v -= v
                    elif k == 1:
                        result += k * 100 * v
                        v -= v
    return result


print(score([5, 1, 3, 4, 1]))
