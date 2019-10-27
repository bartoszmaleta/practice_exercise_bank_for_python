# Write the function translate() that will translate a text into 
# "rövarspråket" (Swedish for "robber's language"). That is, double every 
# consonant and place an occurrence of "o" in between. For example, 
# translate("this is fun") should return the string "tothohisos isos fofunon"


def translate():
    vowels = ("aeiou")
    consonants = ("bcdfghjklmnpqrstvwxyz")
    count = 0
    space = ' '
    letter_o = 'o'
    text = 'this is fun'
    for letter in text:
        if letter in consonants:
            result = letter + letter_o + letter
            print(result,  end='')
            count += 1
        elif letter in vowels:
            print(letter, end='')
            count += 1
        elif letter in space:
            print(space, end='')
            count += 1 

    print()


print()
translate()
print()
print()
