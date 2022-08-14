link = "https://www.codewars.com/kata/52449b062fb80683ec000024"


def generate_hashtag(phrase: str):
    my_list = phrase.split(' ')
    new_list = [i.capitalize() for i in my_list if i != '']
    result = '#' + ''.join(new_list)
    if len(result) >= 140 or result == "#":
        return False
    return result

