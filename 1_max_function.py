# Define a function max() that takes two numbers as arguments and returns the largest of them. 
# Use the if-then-else construct available in Python. (It is true that Python has the max() function 
# built in, but writing it yourself is nevertheless a good exercise.)


def max_out_of_two_arguments(number1, number2):
    print()
    starting_message = 'Your numbers are: >> {} << and >> {} <<'.format(number1, number2)
    print(starting_message)

    if number1 > number2:
        number_of_the_number = 'first'
        greater_number = number1
        message = 'The greater number is {} number and it is: >> {} <<'.format(number_of_the_number, greater_number)
        # print(greater_number)
        return message
    
    if number2 > number1:
        number_of_the_number = 'second'
        greater_number = number2
        message = 'The greater number is {} number and it is: >> {} <<'.format(number_of_the_number, greater_number)
        # print(greater_number)
        return message


max_function = max_out_of_two_arguments(4, 2)
print(max_function)
print()