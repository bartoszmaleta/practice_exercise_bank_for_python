# Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, 
# but writing it yourself is nevertheless a good exercise.)


def print_length_of_given_list_or_string(given_list_or_string):
    counter = 0

    for item in given_list_or_string:
        counter += 1
    
    return counter


list_of_numbers = [2, 4, 5, 6, 8, 9]

example_string = 'this is string'
example_string2 = 'custom'


print('----------------------')
your_item = list_of_numbers
message = 'Your item is >> {} << and the length of it is: '.format(your_item)
len_of_given_item = print_length_of_given_list_or_string(your_item)
print(message)
print(len_of_given_item)

print('+++++++++++++++++')
your_item = example_string
message = 'Your item is >> {} << and the length of it is: '.format(your_item)
len_of_given_item = print_length_of_given_list_or_string(your_item)
print(message)
print(len_of_given_item)

print('+++++++++++++++++')
your_item = example_string2
message = 'Your item is >> {} << and the length of it is: '.format(your_item)
len_of_given_item = print_length_of_given_list_or_string(your_item)
print(message)
print(len_of_given_item)
print('----------------------')
