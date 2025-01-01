def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [0,0,0]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with all zeros is: {average_zero}")

my_list_with_strings = [1,2,"a",4,5]
average_strings = calculate_average(my_list_with_strings)
print(f"The average of a list with strings is: {average_strings}") #This will print the average of numbers only