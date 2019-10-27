# Represent a small bilingual lexicon as a Python dictionary in the following 
# fashion
#  {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
# and use it to translate your Christmas cards from English into Swedish. That is, write 
# a function translate() that takes a list of English words and returns a list of Swedish 
# words.

print()
dictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
list_of_swe_words = []
english_words = ['Merry', 'christmas', 'and', 'happy', 'new', 'year']
print(english_words)


def translate(lst):
    # return [dictionary[w.lower()] for w in lst if w.lower() in dictionary]
    for word in lst:
        if word.lower() in dictionary:
            list_of_swe_words.append(dictionary[word.lower()])

    return list_of_swe_words


print()
# print(list_of_swe_words)
print(translate(english_words))
print()

# ___________________________________________________________________________
# import string

# ignored = string.punctuation + " "
# swedish_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
# list_with_swedish_words = []


# def translate2(list_with_words):
#     word_from_list_of_words = ""
#     translated = ""
#     for word in list_with_words:
#         if not word == " " and not word == ",":
#             word_from_list_of_words += word
#         else:
#             translated += word
#             translated += swedish_dict[word_from_list_of_words]
#             word_from_list_of_words = ""
        
#             list_with_swedish_words.append(translated)
    

#     print(translated)
#     return translated


# text = "merry christmas and happy new year"
# print(translate2(text))
# print(list_with_swedish_words)