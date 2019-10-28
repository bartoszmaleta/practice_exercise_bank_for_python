# Define a function reverse() that computes the reversal of a string. 
# For example, reverse("I am testing") should return the 
# string "gnitset ma I".


text = 'I am testing'


def reverse():
    i = 1
    for letter in text:
        print(text[-i], end='')
        i += 1


print()
reverse()
print()
print()