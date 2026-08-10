class Car:
    print("-> 1. This prints immediately when the Car class is DEFINED.")
    a = 12  # Attribute (no semicolon needed)

    def hello():
        print("Hello World (Method called on the class directly)")


# Accessing the class namespace directly (works because hello() has no 'self')
print(Car.a) 
Car.hello() 


class Bags:
    name = "Mahidi"
    
    def details(self): 
        print(f"This is {self.name}'s company which manufactures bags.")


# Creating instances (objects)
company1 = Bags() 
print(company1.name) 
company1.details() 


class Student:
    print("-> 2. This prints immediately when the Student class is DEFINED.")

    def __init__(self): # Constructor method
        print("-> 3. This constructor runs ONLY when an object is CREATED.")

print("-> 4. About to create a Student object...")
student1 = Student()  # Triggers __init__


class Person:
    def __init__(self, name, age):
        print("-> 5. This constructor runs ONLY when a Person object is CREATED.")

person1 = Person("Mahidi", 25)  # Triggers __init__ with parameters  