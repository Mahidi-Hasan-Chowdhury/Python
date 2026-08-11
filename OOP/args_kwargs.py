def addition(a, b):
    """Returns the sum of two numbers."""
    return a + b

#print (addition(5, 3, 9))  # Error: addition() takes 2 positional arguments but 3 were given

def addition(*args):
    """Returns the sum of all numbers passed as arguments."""
    return sum(args)

print(addition(5, 3))  # Output: 8
print(addition(5, 3, 9))  # Output: 17
print(addition(1, 2, 3, 4, 5))  # Output: 15
# args creates a tuple of all the positional arguments passed to the function, allowing for flexible argument passing.

def info(name,age, **kwargs):
    return kwargs

print(info("Mahidi", 25, city="New York", country="USA", occupation="Engineer"))  # Output: {'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
print(info)  # Output: <function info at 0x7f8c8c8c8c10> (This prints the function object itself, not the result of calling it)




def ExtraGreeting(func):
    def wrapper(*args, **kwargs):
        print("This is an extra greeting before the main function.")
        func(*args, **kwargs)
        print("This is an extra greeting after the main function.")
    return wrapper

@ExtraGreeting
def addition (a,b,c):
    """Returns the sum of three numbers."""
    print(a + b + c)

addition(1, 2, 3)