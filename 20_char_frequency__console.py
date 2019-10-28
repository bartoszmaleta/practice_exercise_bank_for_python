# Write a function char_freq() that takes a string and builds a frequency 
# listing of the characters contained in it. Represent the frequency 
# listing as a Python dictionary. Try it with something like 
# char_freq("abbabcbdbabdbdbabababcbcbab").


def char_freq(str):
    freq = {}
    for character in str:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1
    return freq
      

# test
print()
print(char_freq("abbabcbdbabdbdbabababcbcbab"))
print(char_freq("python"))
print()