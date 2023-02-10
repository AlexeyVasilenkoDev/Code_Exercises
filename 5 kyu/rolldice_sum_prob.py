import itertools

link = "https://www.codewars.com/kata/56f78a42f749ba513b00037f"


def rolldice_sum_prob(sum_of_values, dice_amount):
    cube_values = [1, 2, 3, 4, 5, 6]
    unique_combinations = []
    for i in itertools.product(cube_values, repeat=dice_amount):
        unique_combinations.append((sum(i)))
    return unique_combinations.count(sum_of_values) / len(unique_combinations)
