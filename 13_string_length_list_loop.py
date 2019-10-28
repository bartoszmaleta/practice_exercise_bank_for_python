# Write a program that maps a list of words into a list of integers representing 
# the lengths of the corresponding words.

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

print()
print(list_with_lenghts_of_word)
print()
print()