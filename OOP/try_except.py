# try_except.py
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid integer!")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
finally:
    print("Execution completed.")