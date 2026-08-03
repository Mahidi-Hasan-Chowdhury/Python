# ==============================================================================
# FILE NAME: exam2_operators.py
# PYTHON FOUNDATIONS EXAM - PART 2 (Operators & Expressions)
# INSTRUCTIONS: Answer the questions below directly in this file using comments (#).
# After you are done, copy the entire content of this file and paste it back
# to me in the chat for grading and feedback.
# ==============================================================================

# 1. What will be the output and data type of the following arithmetic expressions?
# a = 10 / 2
# b = 10 // 3
# c = 10 % 3
# d = 2 ** 3
# YOUR ANSWER:
# a = float, 5.0
# b = int, 3
# c = int, 1
# d = int, 8


# 2. Evaluate the following boolean expressions (True or False):
# x = 15
# y = 20
# a = (x < y) and (y == 20)
# b = (x > 20) or (y != 20)
# c = not (x == 15)
# YOUR ANSWER: 
# a = True
# b = False
# c = False


# 3. What is the key difference between the assignment operator (=) and the comparison operator (==)?
# YOUR ANSWER: assignment operator assigns value to variable, and comparison operator compare the true value and return true or false boolean. 


# 4. If you have a variable `score = 10`, write code using an assignment operator 
# (shorthand) that increases its value by 5.
# YOUR ANSWER: score += 5


# 5. MINI-CHALLENGE: 
# Write a short script that:
# 1. Asks a user to enter an integer.
# 2. Uses the modulo operator (%) to check if the number is even.
# 3. Prints a boolean expression result (True if even, False if odd) using a comparison operator.
# YOUR ANSWER:
number = int(input("Enter an integer: "))
if(number%2==0):
    print(True)
else:
    print(False) 

# or simply:
print(number % 2 == 0)    