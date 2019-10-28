# Write a function filter_long_words() that gets a list of 
# words and an integer n and returns the list of words that are longer than n.

list_of_words = ['cattty', 'dog', 'snake', 'frogy']
file_with_list = list_of_words
number_of_letters_in_words = 4
list_with_long_words = []


def filter_long_words(file_with_list, number_of_letters_in_words):
    print()

    list_with_lenghts_of_word = []
    print(list_of_words)
    print(list_with_lenghts_of_word)

    i = 0

    for word in list_of_words:
        item_from_list = list_of_words[i]
        item_from_list = str(item_from_list)
        length_of_word = len(item_from_list)
        list_with_lenghts_of_word.append(length_of_word)
        print(length_of_word, end=' ')
        
        if length_of_word > number_of_letters_in_words:
            list_with_long_words.append(list_of_words[i])

        i += 1
    
    print()
    print(list_with_lenghts_of_word)
    print()
    print(list_with_long_words)


filter_long_words(file_with_list, number_of_letters_in_words)
print()