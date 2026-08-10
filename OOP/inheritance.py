# ==========================================
# PYTHON OBJECT-ORIENTED PROGRAMMING: INHERITANCE
# ==========================================

# --- 1. BASIC & SINGLE INHERITANCE ---
class AnimalParent:
    a = 10

    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is an animal named {self.name}.")


class Humans(AnimalParent):
    pass


print("--- Testing Basic & Single Inheritance ---")
obj2 = Humans("John")
obj2.describe()
print(obj2.a)
print()


# --- 2. SINGLE INHERITANCE WITH METHOD OVERRIDING ---
class BagFactory:
    def __init__(self, material, zip_count, pockets):
        self.material = material
        self.zip_count = zip_count
        self.pockets = pockets

    def details(self):
        print(f"This bag is made of {self.material}, has {self.zip_count} zips, and {self.pockets} pockets.")


class BaggyCompany(BagFactory):  
    def __init__(self, material, zip_count, pockets, color):
        super().__init__(material, zip_count, pockets)
        self.color = color

    def details(self):  
        super().details()  
        print(f"The color of this bag is {self.color}.")


print("--- Testing Single Inheritance with super() ---")
bag2 = BaggyCompany("Canvas", 2, 5, "Red")
bag2.details()
print()


# --- 3. MULTI-LEVEL INHERITANCE ---
class BaggyCompany2(BaggyCompany):  
    def __init__(self, material, zip_count, pockets, color, size):
        super().__init__(material, zip_count, pockets, color)
        self.size = size

    def details(self):
        super().details()  
        print(f"The size of this bag is {self.size}.")


print("--- Testing Multi-Level Inheritance ---")
bag3 = BaggyCompany2("Leather", 3, 4, "Black", "Large")
bag3.details()
print()


# --- 4. HIERARCHICAL INHERITANCE ---
class LivingBeing:
    def breathe(self):
        print("Breathing...")


class Dog(LivingBeing):
    def bark(self):
        print("Woof!")


class Cat(LivingBeing):
    def meow(self):
        print("Meow!")


print("--- Testing Hierarchical Inheritance ---")
dog = Dog()
cat = Cat()
dog.breathe()
cat.breathe()
print()


# --- 5. MULTIPLE INHERITANCE ---
class CarType:
    def __init__(self, brand):
        self.brand = brand

    def car_details(self):
        print(f"This is a car of brand {self.brand}.")


class BikeType:
    def __init__(self, bike_type):
        self.bike_type = bike_type

    def bike_details(self):
        print(f"This is a {self.bike_type} bike.")


class CarBike(CarType, BikeType):  
    def __init__(self, brand, bike_type):
        CarType.__init__(self, brand)
        BikeType.__init__(self, bike_type)


print("--- Testing Multiple Inheritance ---")
obj3 = CarBike("Toyota", "Mountain")
obj3.car_details()
obj3.bike_details()