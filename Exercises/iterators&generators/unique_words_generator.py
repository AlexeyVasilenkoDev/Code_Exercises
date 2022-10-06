from random_word import RandomWords


def unique_words_generator(number_of_words):
    words_limit = 10000
    list_of_words = ['a', 'b', 'c', 'd', 'e']
    assert number_of_words <= words_limit
    word = RandomWords()
    list_of_words = set()
    while len(list_of_words) < number_of_words:
        try:
            new_word = word.get_random_word()
            if new_word in list_of_words:
                new_word = word.get_random_word()
            else:
                list_of_words.add(new_word)
                yield new_word
        except StopIteration as ex:
            raise ex


for i in unique_words_generator(10):
    print(i)
