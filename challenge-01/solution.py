# Problem: Implement a function that takes a list of integers as input and returns the sum of all even numbers in the list.

# Suggested solution


def sum_of_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even


# Test the function
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of even numbers:", sum_of_even_numbers(numbers_list))
