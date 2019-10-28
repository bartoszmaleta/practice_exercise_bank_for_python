# Write a function is_member() that takes a value 
# (i.e. a number, string, etc) x and a list of values a, 
# and returns True if x is a member of a, False otherwise. 
# (Note that this is exactly what the in operator does, but for 
# the sake of the exercise you should pretend Python did not 
# have this operator.)
list_ = ['a', 'b', 'c']
a = 'a'


def is_member(x, a):
    for item in a:
        if item == a:
            return True

    return False


print()
is_member(list_, a)
print()
print()

membering = is_member(list_, a)
print(membering)