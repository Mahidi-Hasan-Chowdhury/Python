# ==============================================================================
# PYTHON FOUNDATIONS EXAM - PART 1
# INSTRUCTIONS: Answer the questions below directly in this file.
# You can use comments (#) to write your answers.
# After you are done, copy the entire content of this file and paste it back
# to me in the chat for grading and feedback.
# ==============================================================================

# 1. Which of the following variable names are INVALID in Python? (Select all that apply)
# A) user_name
# B) 2nd_place
# C) total-amount
# D) _private_var
# E) class
# YOUR ANSWER: A


# 2. Is Python case-sensitive? Would MyVar and myvar be the same variable?
# YOUR ANSWER: Yes, case sensitive. No, not same variable.


# 3. Identify the data type of the following values:
# a = 15.5   -> 
# b = "False" -> 
# c = True    -> 
# d = -100    -> 
# YOUR ANSWER: a: float, b: str, c: boolean, d: int


# 4. Look at the code below. What will be the output of the final line?
# x = "10"
# y = 5
# print(int(x) + y)
# YOUR ANSWER: 15


# 5. What is wrong with this code? How would you fix it using an f-string?
# name = "Agent 001"
# status = "Active"
# print("Agent Name: " + name + " Status: " + status)
# YOUR ANSWER: print(f"Agent Name: {name} Status: {status}")


# 6. If a user runs the following code and types the number 20 into the prompt,
# what will be the data type of the variable 'age'?
# age = input("Enter your age: ")
# YOUR ANSWER: str


# 7. MINI-CHALLENGE: 
# Write a short script that does the following:
# 1. Asks the user for their favorite food.
# 2. Asks the user how many times a week they eat it (this must be a whole number).
# 3. Prints a sentence using an f-string: 
#    "You love [food] so much that you eat it [number] times a week!"
# YOUR ANSWER:
food = input("What is your favorite food: ")
number = int(input("How many times a week do you eat it: "))
print(f"You love {food} so much that you eat it {number} times a week.") 