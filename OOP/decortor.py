def ExtraGreeting(func):
    def wrapper():
        print("This is an extra greeting before the main function.")
        func()
        print("This is an extra greeting after the main function.")
    return wrapper


@ExtraGreeting    
def greet():
    print("Hello, welcome to the program!")

greet()  # Output: Hello, welcome to the program!    