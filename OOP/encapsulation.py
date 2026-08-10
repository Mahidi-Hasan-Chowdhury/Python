class Animal:
    a = 12
print(Animal.a)  # Accessing the class attribute directly    
# This will print 12 because we are accessing the class attribute 'a' directly from the class 'Animal'.


class Factory:
    name = "Kingdom Factory"  # Public class attribute
    _old = 12 # Protected class attribute
    def __init__(self, type, tyre, color): 
        self.type = type # Public instance attribute
        self.tyre = tyre
        self.color = color

    def details(self): #public method
        print(f"This is a {self.type} with {self.tyre} tyres and it is {self.color} in color.")    

obj = Factory("Car", 4, "Red")
print(obj.name)  # Accessing the public class attribute through an instance  
obj.name = "New Factory Name"  # Modifying the public class attribute through an instance
print(obj.name)  # Accessing the modified public class attribute through the instance      
obj2 = Factory("Bike", 2, "Blue")
print(obj2.name)  # Output: "Kingdom Factory" (It still points to the class attribute!)
print(Factory.name)  # Output: "Kingdom Factory"
Factory.name = "Updated Factory Name"  # Modifying the class attribute directly
print(Factory.name)  # Output: "Updated Factory Name"


print(obj._old)  # Accessing the protected class attribute through an instance (not recommended, but possible)
print(Factory._old)  # Accessing the protected class attribute directly from the class (not recommended, but possible)



# ==========================================
# PYTHON ENCAPSULATION: PRIVATE & GETTERS/SETTERS
# ==========================================

class BankAccount:
    __a = 12
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (double underscore)

    # 1. Getter Method: Safely read the private balance
    def get_balance(self):
        return self.__balance

    # 2. Setter Method: Safely modify the private balance with rules
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Error: Invalid withdrawal amount or insufficient funds!")



#print(BankAccount.a)  # Accessing the class attribute directly
#AttributeError: type object 'BankAccount' has no attribute 'a'

#print(BankAccount.__a)  # Trying to access the private class attribute directly will raise an AttributeError

account = BankAccount("Mahidi", 1000)
print(account.owner)  # Accessing the public attribute works fine
#print(account.__balance)  # Trying to access the private attribute directly WILL CRASH: AttributeError: 'BankAccount' object has no attribute '__balance'
print(account.get_balance())  # Accessing the private attribute through the getter method works fine

# --- Testing Encapsulation ---
print("--- Testing Bank Account Encapsulation ---")
my_account = BankAccount("Mahidi", 1000)

# Accessing public attribute works fine
print(f"Account Owner: {my_account.owner}")

# Trying to access private attribute directly WILL CRASH:
# print(my_account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Using Getter and Setter methods to interact with the private data safely:
print(f"Initial Balance: ${my_account.get_balance()}")

my_account.deposit(500)    # Uses setter logic
my_account.withdraw(200)   # Uses setter logic

# Note on Name Mangling: 
# Python actually renamed '__balance' internally to '_BankAccount__balance'.
# You *can* technically cheat and access it like this, but it violates OOP rules!
print(my_account._BankAccount__balance)


class hello:
    __a = 12
    @classmethod
    def get_a(cls):
        print(cls.__a)  # Accessing the private class attribute through a class method
obj = hello()
obj.get_a()  # Output: 12

class hello2(hello):
    print(hello._hello__a)  # Accessing the protected class attribute from the parent class (not recommended, but possible)