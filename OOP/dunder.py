class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"    

    def describe(self):
        return f"{self.name} is an animal."

obj = Animal("Lion")
obj.describe()  # Output: Lion is an animal.
print(obj)  # Output: Animal: Lion

obj2 = Animal("Tiger")
print(obj2)  # Output: Animal: Tiger


class Numbers:
    def __init__(self,num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    def __eq__(self, other):
        return self.num == other.num

num1 = Numbers(5)
num2 = Numbers(5)
print(num1 + num2)  # This will raise a TypeError because the '+' operator is not defined for the Numbers class.     
print(num1 == num2)  # This will raise a TypeError because the '==' operator is not defined for the Numbers class.   


a = 12
print(type(a))  # Output: <class 'int'>
print(dir(a))  # Output: List of all attributes and methods of the int class