# Define a function sum() and a function multiply() that sums and 
# multiplies (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) 
# should return 24.

list_of_numbers = [1, 2, 3, 4]

def sums_items_of_list(your_item):
    result_of_suming = 0

    for num in list_of_numbers:
        result_of_suming += num
    
    print(result_of_suming)
    return result_of_suming


# your_item = list_of_numbers
sums_items_of_list(list_of_numbers)
