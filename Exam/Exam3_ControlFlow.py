# ==============================================================================
# FILE NAME: exam3_control_flow.py
# PYTHON FOUNDATIONS EXAM - PART 3 (Control Flow & Conditionals)
# INSTRUCTIONS: Answer the questions below directly in this file using comments (#).
# After you are done, copy the entire content of this file and paste it back
# to me in the chat for grading and feedback.
# ==============================================================================

# 1. Look at the code snippet below. What will be printed to the console?
# x = 10
# if x > 15:
#     print("A")
# elif x > 5:
#     print("B")
# else:
#     print("C")
# YOUR ANSWER: B


# 2. Why is indentation critical in Python when writing conditional blocks? 
# What error does Python throw if indentation is incorrect?
# YOUR ANSWER: It determines the scope of the code block, and if indentation is incorrect, Python throws an IndentationError. 


# 3. Fill in the missing parts of the conditional statement below so that it prints 
# "Hot" if temperature is greater than 30, "Warm" if between 20 and 30 (inclusive), 
# and "Cold" otherwise.
# temperature = 25
# if (temperature > 30):
#     print("Hot")
# elif (temperature >= 20 and temperature <= 30):
#     print("Warm")
# else:
#     print("Cold")


# 4. MINI-CHALLENGE:
# Write a short script that:
# 1. Asks the user for their age (convert it to an integer).
# 2. If the age is less than 13, print "Child".
# 3. If the age is between 13 and 19 (inclusive), print "Teenager".
# 4. If the age is 20 or older, print "Adult".
# YOUR ANSWER:
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")