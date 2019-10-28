# Define a function overlapping() that takes two lists and returns True 
# if they have at least one member in common, False otherwise. 
# You may use your is_member() function (previous exercise), or the in 
# operator, but for the sake of the exercise, you should (also) 
# write it using two nested for-loops.

list_of_items = ['a', 'b', 'c', 'd']
list_of_items2 = ['b', 'e', 'g']
helping_list_for_list_of_items = []
helping_list_for_list_of_items2 = []


def overlapping(list_of_items, list_of_items2):
    for item in list_of_items:
        if item in list_of_items2:
            return True

    return False


print()
overlapping(list_of_items, list_of_items2)

membering = overlapping(list_of_items, list_of_items2)
print(membering)

print()