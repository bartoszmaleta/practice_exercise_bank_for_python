# "99 Bottles of Beer" is a traditional song in the United States and Canada. 
# It is popular to sing on long trips, as it has a very repetitive format 
# which is easy to memorize and can take a long time to sing. The song's 
# simple lyrics are as follows:

# > 99 bottles of beer on the wall, 99 bottles of beer.
# > Take one down, pass it around, 98 bottles of beer on the wall.

# The same verse is repeated, each time with one fewer bottle. The song is 
# completed when the singer or singers reach zero.
# Your task here is to write a Python program capable of generating all the 
# verses of the song.

number_of_bottles = 99


while number_of_bottles > 0:
    print('{} bottles of beer on the wall, {} bottles of beer.'.format(number_of_bottles, number_of_bottles))
    number_of_bottles -= 1
    print('Take one down, pass it around, {} bottles of beer on the wall.'.format(number_of_bottles))


