link = "https://www.codewars.com/kata/562e6df5cf2d3908ad00019e"


def separate_liquids(glass):
    density = {
        "H": 1.36,
        "W": 1.00,
        "A": 0.87,
        "O": 0.8,
    }
    result = []
    for i in glass:
        result.extend(*[i])
    result.sort(key=lambda x: density[x])
    for i in range(len(glass)):
        batch_size = len(glass[0])
        result.append(result[:batch_size])
        result = result[batch_size:]
    return result
