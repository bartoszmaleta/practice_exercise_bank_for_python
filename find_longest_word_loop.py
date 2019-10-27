# Write a function find_longest_word() that takes a list of words and 
# returns the length of the longest one.

list_of_words = ['cat', 'dog', 'snake', 'frog']
file_with_list = list_of_words


def find_longest_word(file_with_list):
    print()

    list_of_words = ['cat', 'dog', 'snake', 'frog']
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
        i += 1

    index = 0
    print()
    best_length = list_with_lenghts_of_word[index]

    for length in list_with_lenghts_of_word:
        if length > best_length:
            best_length = length
            index += 1

    print(list_with_lenghts_of_word)
    print()

    print('The length of the longest word is: ', best_length)
    print()


find_longest_word(file_with_list)