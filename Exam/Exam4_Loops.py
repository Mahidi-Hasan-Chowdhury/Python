# ==============================================================================
# FILE NAME: exam4_loops.py
# PYTHON FOUNDATIONS EXAM - PART 4 (Loops & Iteration)
# INSTRUCTIONS: Answer the questions below directly in this file using comments (#).
# After you are done, copy the entire content of this file and paste it back
# to me in the chat for grading and feedback.
# ==============================================================================

# 1. What is the main difference between a `for` loop and a `while` loop in Python?
# YOUR ANSWER: a for loop is a loop when start and end is defined and in a certain range we know. While loop is a loop that runs indefinitely before a certain condition is met.


# 2. Look at the code snippet below. How many times will "Hello" be printed?
# count = 0
# while count < 3:
#     print("Hello")
#     count += 1
# YOUR ANSWER: 3


# 3. What do the `break` and `continue` keywords do inside a loop?
# YOUR ANSWER: break stops the loop immediately and return to the next line of code. Continue skips the current iteration if a condition met. 


# 4. MINI-CHALLENGE:
# Write a short script using a `for` loop and `range()` that:
# 1. Loops from 1 to 10 (inclusive).
# 2. Prints only the **even** numbers (Hint: you can use an `if` statement with `%` inside the loop).
# YOUR ANSWER: 
for i in range(1,11):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)