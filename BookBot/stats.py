def count_words(text):
    return len(text.split())


def count_characters(text):
    dictionary = {}

    for char in text:
        lower_char = char.lower()
        if lower_char in dictionary:
            dictionary[lower_char] += 1
        else:
            dictionary[lower_char] = 1

    return dictionary

def sort_on(dict):
    return dict["num"]

def sort_dictionary(characters):
    temp_list = []
    keys = characters.keys()
    for key in keys:
        temp_list.append({"key": key, "num": characters[key]})
    temp_list.sort(reverse=True, key = sort_on)
    return temp_list