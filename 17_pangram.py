# A pangram is a sentence that contains all the letters of the English 
# alphabet at least once, for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

import string

print()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = 'The quick brown fox jumps over the lazy dog.'
string_with_text = text
number_of_letters_in_alphabet = len(alphabet)
print('number of letters in alphabet: ', number_of_letters_in_alphabet) 
ignored = string.punctuation + ' '


def panagram(string_with_text):
    cleanstr = ''
    counter = 0
    for letter in string_with_text:
        if letter in ignored:
            cleanstr += ''
        else:
            cleanstr += letter.lower()
        # print(cleanstr)
    
    for char in alphabet:
        if char in cleanstr:
            counter += 1
            # return False
    print('number of letters of sentence in alphabet: ', counter)

    if counter == 26:
        return True
    else:
        return False
    # return True

    # print(cleanstr)
    # return cleanstr
        

panagram_func = panagram(string_with_text)
print()
print(panagram_func)
print()
print('-----------------')
string_with_text = 'Example string'
panagram_func2 = panagram(string_with_text)
print(panagram_func2)
print()