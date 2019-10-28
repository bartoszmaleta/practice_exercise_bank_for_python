# Define a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written backwards). 
# For example, is_palindrome("radar") should return True.

print()
text = 'radar'
print('----------------')
print('Text: ', text)
print('----------------')
list_of_reversed_letters = []
list_of_letters_in_text = []


def is_palindrom():
    reverse()
    print()
    for letter in text:
        list_of_letters_in_text.append(letter)

    if list_of_letters_in_text == list_of_reversed_letters:
        return True


def reverse():
    i = 1
    message = 'Reversed text: '
    print(message)
    print()
    for letter in text:
        reversed_letter = text[-i]
        print(reversed_letter, end='')
        list_of_reversed_letters.append(reversed_letter)
        i += 1


# print(list_of_reversed_letters)
# print(list_of_letters_in_text)

print('----------------')
checking_palindrom = is_palindrom()
print(checking_palindrom)