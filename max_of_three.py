# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.


def max_of_three(number1, number2, number3):
    list_of_three_numbers = []
    list_of_three_numbers.append(number1)
    list_of_three_numbers.append(number2)
    list_of_three_numbers.append(number3)
    # print(list_of_three_numbers)
    
    best = list_of_three_numbers[0]

    for num in list_of_three_numbers:
        if num > best:
            best = num

    # print(best)
    return best


first_number = 2
second_number = 3
third_number = 5
max_of_three(first_number, second_number, third_number)

print()
print()

greatest_out_of_three = max_of_three(2, 3, 5)
print('The greatest out of these numbers >> {} <<  >> {} <<  >> {} << is:'.format(first_number, second_number, third_number))
print(greatest_out_of_three)