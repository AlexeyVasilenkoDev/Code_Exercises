from random_word import RandomWords


def unique_words_generator(number_of_words):
    word = RandomWords()
    list_of_words = set()
    while len(list_of_words) < number_of_words:
        try:
            new_word = word.get_random_word()
            list_of_words.add(new_word)
            yield new_word
        except StopIteration as ex:
            raise ex


for i in unique_words_generator(10):
    print(i)
