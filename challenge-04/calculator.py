# Problem: Create a Python module called "calculator" that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division). Implement error handling to handle division by zero.

# Proposed solution


# calculator.py
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero!"
    else:
        return result
