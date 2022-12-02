link = "https://www.codewars.com/kata/5264d2b162488dc400000001"


def spin_words(sentence):
    result_list = sentence.split()
    if len(result_list) > 1:
        return " ".join(i[::-1] if len(i) >= 5 else i for i in result_list)
    return sentence[::-1] if len(sentence) >= 5 else sentence


print(spin_words("This sentence is a sentence"))
