# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******
print()
list_of_integers = [1, 2, 3, 4, 5]
list_file = list_of_integers


def histogram(list_file):
    sign_to_print = '*'
    i = 0

    for item in list_of_integers:
        print(list_file[i])
        operation = sign_to_print * list_file[i]
        print(operation)
        i += 1


histogram(list_of_integers)
print()