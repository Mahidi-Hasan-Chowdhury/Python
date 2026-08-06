# ==============================================================================
# FILE NAME: exam6_functions.py
# PYTHON FOUNDATIONS EXAM - PART 6 (Functions & Scope)
# ==============================================================================

# 1. What is the main difference between `print()` and `return` inside a function?
# ANSWER: 
# `print()` simply displays text on the screen for a human to see; the computer 
# cannot reuse that data. `return` sends data back out of the function so it can 
# be stored in a variable, processed, or passed to other parts of your program.


# 2. Look at the function below. What value does it output/send back when called?
# def add(a, b):
#     result = a + b
#     return result
# ANSWER: 
# It evaluates to and returns `7` (when called like `add(3, 4)`). If you assign it 
# to a variable (`sum_val = add(3, 4)`), `sum_val` will hold the integer `7`.


# 3. What is the difference between a local variable and a global variable?
# ANSWER: 
# A local variable is created *inside* a function and only exists while that function 
# is running (it cannot be accessed outside of it). A global variable is created at 
# the main level of the script and can be accessed anywhere in the file.


# 4. MINI-CHALLENGE:
# Write a function named `is_even` that takes a number as a parameter, 
# uses the modulo operator to check if it's even, and returns `True` or `False`.
# ANSWER:
def is_even(num):
    return num % 2 == 0

# Example usage:
# print(is_even(4))  # Returns True
# print(is_even(5))  # Returns False