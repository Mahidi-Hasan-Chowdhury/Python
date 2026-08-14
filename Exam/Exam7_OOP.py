# ==============================================================================
# PYTHON ADVANCED EXAM — OBJECT-ORIENTED & FUNCTIONAL PYTHON
# TOPICS: Classes, Encapsulation, Inheritance, Polymorphism, Abstraction, 
#         Dunder Methods, Decorators, *args/**kwargs, Lambdas, Map/Filter/Zip
# ==============================================================================
# INSTRUCTIONS:
#   - Answer theory questions using comments (#).
#   - Write code directly under `# YOUR CODE:`.
#   - Share this file when done for grading!
# ==============================================================================


# ==============================================================================
# QUESTION 1: CLASSES, ATTRIBUTES & METHODS (15 pts)
# ==============================================================================
# Create a class named `SmartPhone`:
#   1. Has a class attribute `operating_system = "Android"`.
#   2. Has an `__init__` constructor taking `brand` and `price`.
#   3. Has an instance method `get_info()` returning: "[brand] costs $[price]."
#   4. Has a `@classmethod` named `update_os(cls, new_os)` that changes `operating_system`.
#   5. Has a `@staticmethod` named `is_valid_price(price)` returning True if price > 0, else False.
# YOUR CODE:




# ==============================================================================
# QUESTION 2: ENCAPSULATION & PRIVATE DATA (15 pts)
# ==============================================================================
# Create a class `UserAccount`:
#   1. Private attribute `__password` set in `__init__`.
#   2. Public attribute `username` set in `__init__`.
#   3. A method `check_password(input_pwd)` that returns True if it matches `__password`.
#   4. A setter method `change_password(old_pwd, new_pwd)` that updates `__password`
#      ONLY if `old_pwd` matches the current password and `len(new_pwd) >= 6`.
# YOUR CODE:




# ==============================================================================
# QUESTION 3: INHERITANCE & SUPER() (15 pts)
# ==============================================================================
# 1. Base Class `Vehicle`: `__init__` takes `brand` and `speed`.
#    Method `move()` prints "Vehicle [brand] is moving at [speed] km/h."
# 2. Child Class `ElectricCar` inheriting from `Vehicle`:
#    - `__init__` takes `brand`, `speed`, and `battery_capacity`.
#    - Uses `super().__init__()` to initialize `brand` and `speed`.
#    - Overrides `move()` to call `super().move()` AND print "Battery capacity: [battery_capacity] kWh."
# YOUR CODE:




# ==============================================================================
# QUESTION 4: ABSTRACTION & POLYMORPHISM (15 pts)
# ==============================================================================
# 1. Create an abstract class `AIAgent` using `ABC` with an `@abstractmethod` named `process_task(self, prompt)`.
# 2. Create class `ChatAgent(AIAgent)` that implements `process_task` -> returns "ChatAgent responding to: [prompt]".
# 3. Create class `CodeAgent(AIAgent)` that implements `process_task` -> returns "CodeAgent generating code for: [prompt]".
# 4. Demonstrate polymorphism by placing both agents in a list and calling `process_task("Fix bug")` in a loop.
# YOUR CODE:




# ==============================================================================
# QUESTION 5: DUNDER METHODS (10 pts)
# ==============================================================================
# Create a class `Product` taking `name` and `price`:
#   1. Implement `__str__` to return "Product: [name] ($[price])".
#   2. Implement `__add__` so that adding two Product objects returns the sum of their prices.
#      Example: p1 = Product("Mouse", 20), p2 = Product("Keyboard", 50) -> p1 + p2 returns 70
# YOUR CODE:




# ==============================================================================
# QUESTION 6: DECORATORS & *ARGS / **KWARGS (15 pts)
# ==============================================================================
# 1. Create a decorator `log_execution(func)` that:
#    - Prints "--- Starting execution ---" before running the function.
#    - Runs the target function passing `*args` and `**kwargs`.
#    - Prints "--- Finished execution ---" after running.
# 2. Apply `@log_execution` to a function `calculate_total(*prices, discount=0)` 
#    which prints the sum of `prices` minus `discount`.
# YOUR CODE:




# ==============================================================================
# QUESTION 7: LAMBDAS, MAP, FILTER & COMPREHENSIONS (15 pts)
# ==============================================================================
# Given list: numbers = [12, 5, 8, 19, 24, 3, 30]
#   1. Use `filter()` with a `lambda` to extract all numbers > 10. (Store in list `above_ten`)
#   2. Use `map()` with a `lambda` to double all numbers in `above_ten`. (Store in list `doubled`)
#   3. Rewrite both steps in ONE line using a List Comprehension.
# YOUR CODE:




# ==============================================================================
# END OF OOP EXAM
# Total: 100 pts
# Share this file when finished!
# ==============================================================================
