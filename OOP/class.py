class Car:
    print("-> 1. This prints immediately when the Car class is DEFINED.")
    a = 12  # Attribute (no semicolon needed)

    def hello():
        print("Hello World (Method called on the class directly)")


# Accessing the class namespace directly (works because hello() has no 'self')
print(Car.a) 
Car.hello() 

# 2. THIS WILL CRASH!
#my_car = Car()
#my_car.hello()  # TypeError: hello() takes 0 positional arguments but 1 was given


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
        print(f"-> 6. The name is {name} and the age is {age}.")

person1 = Person("Mahidi", 25)  # Triggers __init__ with parameters 
person2 = Person("John", 30)  # Triggers __init__ with different parameters
#print(person1.name)  # Trying to access the name attribute of person1 will raise an AttributeError because we haven't stored the name in the object.
#print(person2.name)  # Trying to access the name attribute of person2 will also raise an AttributeError for the same reason.


# Self is a reference to the current instance of the class and is used to access variables that belong to the class. It must be the first parameter of any function in the class. 
# person1 and person2 are two different instances of the Person class, each with its own name and age attributes.
# Self is the address of the object in memory, and it allows us to access the attributes and methods of the class for that specific instance.
#Ex: person1 has the memory address of 100, and person2 has the memory address of 200. When we call person1.name, it accesses the name attribute of the object at memory address 100, which is "Mahidi". When we call person2.name, it accesses the name attribute of the object at memory address 200, which is "John".
# So, it saves the memory address of the object in memory, and it allows us to access the attributes and methods of the class for that specific instance.



# But we currently the value of the attributes are not stored in the object, they are just printed in the constructor. To store the values in the object, we need to use self.name and self.age to assign the values to the instance variables.

class toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def details(self):
        print(f"This is a {self.name} toy and it costs ${self.price}.")

toy1 = toy("Teddy Bear", 19.99)
toy2 = toy("Lego Set", 49.99)
toy1.details()  # This is a Teddy Bear toy and it costs $19.99
toy2.details()  # This is a Lego Set toy and it costs $49.99



# ==============================================================================
# PYTHON OOP: ATTRIBUTES AND METHODS MASTER CLASS
# ==============================================================================

class Robot:
    # --------------------------------------------------------------------------
    # 1. CLASS ATTRIBUTE
    # Defined directly inside the class, outside any function.
    # SHARED by ALL instances of this class. If you change it for the class,
    # it changes for every robot object.
    # --------------------------------------------------------------------------
    battery_type = "Lithium-ion"

    def __init__(self, name, model):
        # ----------------------------------------------------------------------
        # 2. INSTANCE ATTRIBUTES
        # Defined inside the __init__ constructor using 'self'.
        # UNIQUE to each specific object (instance). robot1 has its own name/model;
        # robot2 has its own. They do not share these specific values.
        # ----------------------------------------------------------------------
        self.name = name
        self.model = model

    # --------------------------------------------------------------------------
    # 3. INSTANCE METHOD
    # Operates on a SPECIFIC object instance.
    # Must take 'self' as the first parameter to access that object's data.
    # --------------------------------------------------------------------------
    def introduce(self):
        # Uses 'self.name' and 'self.model' which belong to THIS specific robot object
        print(f"I am {self.name}, model {self.model}.")

    # --------------------------------------------------------------------------
    # 4. CLASS METHOD (@classmethod)
    # Operates on the CLASS itself, rather than a single individual instance.
    # Uses the '@classmethod' decorator and takes 'cls' instead of 'self'.
    # Can view and modify class attributes globally.
    # --------------------------------------------------------------------------
    @classmethod
    def update_battery(cls, new_type):
        cls.battery_type = new_type  # Modifies the shared class attribute
        print(f"Global battery type updated to: {cls.battery_type}")

    # --------------------------------------------------------------------------
    # 5. STATIC METHOD (@staticmethod)
    # A standalone utility function that happens to live inside the class namespace.
    # Does NOT take 'self' or 'cls'. It has zero access to instance or class data.
    # Used for independent helper tasks related to the class theme.
    # --------------------------------------------------------------------------
    @staticmethod
    def validate_code(code):
        return code == 9999


# ==============================================================================
# EXECUTION & TESTING
# ==============================================================================

# Creating distinct robot instances (objects)
bot1 = Robot("Alpha", "X-1")
bot2 = Robot("Beta", "X-2")

# 1. Calling an Instance Method (uses bot1's unique instance data)
bot1.introduce()  # Output: I am Alpha, model X-1.

# 2. Calling a Class Method (changes the setting for the entire class)
Robot.update_battery("Solid-state")  

# 3. Calling a Static Method (runs a helper check without needing an object)
is_valid = Robot.validate_code(9999)
print(f"Is security code valid? {is_valid}")