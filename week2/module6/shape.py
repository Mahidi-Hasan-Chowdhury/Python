from math import pi
class shape:
    def __init__(self,name):
        self.name = name
    def read(self):
        raise NotImplementedError
class rectangle(shape):
    def __init__(self, name,length,width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class circle(shape):
    def __init__(self, name,radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius*self.radius
    def read(self):
        print('Reading')

circle1 = circle('Circle',2)

print(issubclass(circle,shape))
print(isinstance(circle1,circle))
print(isinstance(circle1,shape))

circle1.read()