class animals:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        print('Animal Making Some Sound')

class cat(animals):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('Meow Meow')

class Dog(animals):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('GHEW GHEW')

class Goat(animals):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('Beh Beh')

don = cat('Real Don')
don.make_sound()

shepard = Dog('Local shepard')
shepard.make_sound()

goat1 = Goat("Mahidi")
goat2 = Goat("Siam")
goat1.make_sound()

animals = [don,shepard,goat1,goat2]

for animal in animals:
    animal.make_sound()