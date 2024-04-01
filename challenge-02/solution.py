# Problem: Write a Python program to check whether a number is prime or not..


# Proposed Solution
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Test the function
num = 13
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
