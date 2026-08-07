# ==============================================================================
# PYTHON FOUNDATIONS — FINAL REVIEW EXAM
# TOPICS: Variables, Operators, Control Flow, Loops, Data Structures, Functions
# INSTRUCTIONS:
#   - Answer every question using comments (#) unless told to write code.
#   - For coding questions, write your code BELOW the # YOUR CODE: line.
#   - Do NOT look at your previous exams. Test your real memory!
#   - When done, share this file for grading and feedback.
# ==============================================================================


# ==============================================================================
# SECTION 1 — VARIABLES & DATA TYPES (20 pts)
# ==============================================================================

# Q1. What will be printed by the following code? (2 pts)
# x = "5"
# y = 5
# print(x == y)
# YOUR ANSWER: False


# Q2. What data type is each of these? (4 pts)
# a = 3.14       -> float
# b = "True"     -> string
# c = False      -> boolean
# d = 100        -> integer
# YOUR ANSWER:


# Q3. What is wrong with this variable name? Why? (2 pts)
# 3d_model = "cube"
# YOUR ANSWER: Variable names cannot start with a number.


# Q4. What will the output be? (2 pts)
# name = "Mahedi"
# age = 22
# print(f"My name is {name} and I am {age} years old.")
# YOUR ANSWER: My name is Mahedi and I am 22 years old.


# Q5. CODING — Write a script that: (10 pts)
#   1. Asks the user for their name.
#   2. Asks the user for their birth year (convert to integer).
#   3. Calculates their age (assume current year is 2026).
#   4. Prints: "Hello [name]! You are [age] years old."
# YOUR CODE:
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"Hello {name}! You are {age} years old.")



# ==============================================================================
# SECTION 2 — OPERATORS (15 pts)
# ==============================================================================

# Q6. What is the output and data type of each? (4 pts)
# a = 17 // 4    ->
# b = 17 % 4     ->
# c = 2 ** 4     ->
# d = 15 / 3     ->
# YOUR ANSWER: a = 4 (integer), b = 1 (integer), c = 16 (integer), d = 5.0 (float)


# Q7. Evaluate these boolean expressions. x = 8, y = 12 (6 pts)
# a = (x < y) and (y > 10)         ->
# b = (x == 8) or (y == 8)         ->
# c = not (x > 5)                  ->
# d = (x != y) and not (y == 12)   ->
# YOUR ANSWER: a = True, b = True, c = False, d = False


# Q8. CODING — Write ONE line of code that: (5 pts)
#   Takes a variable score = 95 and increases it by 5 using a shorthand operator.
#   Then prints the result.
# YOUR CODE:
score = 95



# ==============================================================================
# SECTION 3 — CONTROL FLOW (15 pts)
# ==============================================================================

# Q9. What will be printed? (3 pts)
# temperature = 22
# if temperature > 35:
#     print("Very Hot")
# elif temperature > 25:
#     print("Hot")
# elif temperature > 15:
#     print("Warm")
# else:
#     print("Cold")
# YOUR ANSWER: warm


# Q10. What error does Python throw for incorrect indentation? (2 pts)
# YOUR ANSWER: IndentationError


# Q11. CODING — Write a script that: (10 pts)
#   1. Asks the user to enter a number.
#   2. If the number is positive, print "Positive".
#   3. If the number is negative, print "Negative".
#   4. If the number is zero, print "Zero".
# YOUR CODE: 
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")




# ==============================================================================
# SECTION 4 — LOOPS (20 pts)
# ==============================================================================

# Q12. How many times will "Python" be printed? (3 pts)
# i = 1
# while i <= 5:
#     print("Python")
#     i += 2
# YOUR ANSWER: 3 times


# Q13. What will be the output of this code? (4 pts)
# for i in range(2, 10, 3):
#     print(i)
# YOUR ANSWER: 2, 5, 8


# Q14. What does `break` do differently from `continue`? (3 pts)
# YOUR ANSWER: `break` exits the loop completely, while `continue` skips the current iteration and moves to the next one.


# Q15. CODING — Write a script that: (10 pts)
#   1. Uses a while loop.
#   2. Starts at 10 and counts DOWN to 1.
#   3. Skips the number 5 (use continue).
#   4. Prints each number.
# YOUR CODE:





# ==============================================================================
# SECTION 5 — DATA STRUCTURES (15 pts)
# ==============================================================================

# Q16. Fill in the blanks: (3 pts)
# List     = ordered, __________ (can/cannot be changed)
# Tuple    = ordered, __________ (can/cannot be changed)
# Set      = __________, only stores unique items
# YOUR ANSWER:


# Q17. What will be the output? (4 pts)
# info = {"name": "Ali", "age": 25, "city": "Dhaka"}
# info["age"] = 26
# info["job"] = "Engineer"
# print(info["city"])
# print(len(info))
# YOUR ANSWER:


# Q18. CODING — Write a script that: (8 pts)
#   1. Creates a list of 5 numbers: [10, 20, 30, 40, 50]
#   2. Loops through the list using a for loop.
#   3. Prints only the numbers greater than 25.
# YOUR CODE:




# ==============================================================================
# SECTION 6 — FUNCTIONS (15 pts)
# ==============================================================================

# Q19. What is the difference between print() and return in a function? (3 pts)
# YOUR ANSWER:


# Q20. What will this code output? (4 pts)
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"
#
# print(greet("Sara"))
# print(greet("Omar", "Hi"))
# YOUR ANSWER:


# Q21. CODING — Write a function that: (8 pts)
#   1. Is named calculate_bmi.
#   2. Takes two parameters: weight (kg) and height (meters).
#   3. Calculates BMI using the formula: BMI = weight / (height ** 2)
#   4. Returns "Underweight" if BMI < 18.5
#   5. Returns "Normal" if BMI is between 18.5 and 24.9
#   6. Returns "Overweight" if BMI >= 25
#   7. Call the function and print the result.
# YOUR CODE:




# ==============================================================================
# BONUS CHALLENGE — (10 pts) — Optional but HIGHLY recommended!
# ==============================================================================

# CODING — Build a simple Number Guessing Game:
#   1. Create a variable secret_number = 7  (hardcode it, no random needed)
#   2. Use a while loop that keeps running until the user guesses correctly.
#   3. Ask the user to enter a guess (convert to integer).
#   4. If guess is too low  -> print "Too low! Try again."
#   5. If guess is too high -> print "Too high! Try again."
#   6. If guess is correct  -> print "Correct! You got it!" and stop the loop.
# YOUR CODE:




# ==============================================================================
# END OF EXAM
# Total: 100 pts + 10 bonus pts
# When done, share this file and I will grade every single answer!
# ==============================================================================
