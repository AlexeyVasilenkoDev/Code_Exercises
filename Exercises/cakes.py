import math

link = "https://www.codewars.com/kata/525c65e51bf619685c000059"


def cakes(recipe, available):
    number_of_cakes = []
    for k, v in available.items():
        if k in recipe.keys():
            number_of_cakes.append(math.floor(available[k] / recipe[k]))
    for k, v in recipe.items():
        if k not in available.keys():
            return 0
    return min(number_of_cakes)
