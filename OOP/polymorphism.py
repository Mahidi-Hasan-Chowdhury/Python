class animal:
    def speak(self):
        print("Animal not speaks")

class humans:
    def speak(self):
        print("Humans speak")

obj1 = animal()
obj2 = humans()        

obj1.speak()
obj2.speak()
# In this case polymorphism is achieved by having the same method name 'speak' in both classes, but with different implementations. When we call the 'speak' method on an instance of each class, it executes the respective implementation based on the object's class.

# Method Overriding: In the context of inheritance, polymorphism can also be achieved through method overriding. When a subclass provides a specific implementation of a method that is already defined in its superclass, it overrides the superclass's method. This allows the subclass to provide its own behavior while still maintaining the same method signature.

class person: 
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is a person named {self.name}.")

class student(person):
    def describe(self):
        print(f"This is a student named {self.name}.")

obj = student("Mahidi")  
obj.describe()  # This will call the overridden method in the student class, demonstrating polymorphism through method overriding.

obj1 = person("John")
obj1.describe()  # This will call the describe method in the person class, demonstrating polymorphism through method overriding as well.


#Method Overloading: Python does not support method overloading in the traditional sense (like in some other languages), where multiple methods can have the same name but different parameter lists. However, we can achieve similar behavior using default arguments or variable-length arguments.

class hello:
    def speak(self,a):
        print(f"Hello {a}")

    def speak(self,a,b):
        print(f"Hello {a} and {b}")    

now = hello()
now.speak("Mahidi","John")  # This will call the second speak method,        
# but if we try to call now.speak("Mahidi"), it will raise a TypeError because the first speak method is overridden by the second one.


class Hello:
    # Using a default argument (b = None) to handle 1 or 2 parameters
    def speak(self, a, b=None):
        if b is None:
            print(f"Hello {a}")
        else:
            print(f"Hello {a} and {b}")

now = Hello()
now.speak("Mahidi")          # Works! Output: Hello Mahidi
now.speak("Mahidi", "John")  # Works! Output: Hello Mahidi and John