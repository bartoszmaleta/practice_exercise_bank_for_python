# The function max() and the function max_of_three() from previous exercises will only 
# work for two and three numbers, respectively. But suppose we have a much larger 
# number of numbers or suppose we cannot tell in advance how many there are? 
# Write a function max_in_list() that takes a list of numbers and returns the largest one.

list_of_numbers = [1, 2, 3, 4]
filelist = list_of_numbers


def max_in_list(filelist):
    # print(list_of_three_numbers)
    
    best = list_of_numbers[0]

    for num in list_of_numbers:
        if num > best:
            best = num

    # print(best)
    return best


print()
print()
max_number_out_filelist = max_in_list(list_of_numbers)
print(max_number_out_filelist)
print()