class person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('Rice, Mutton,Noodles')
        
    def exercise(self):
        raise NotImplementedError

class cricketer(person):
    def __init__(self,name,age,height,weight,team)->None:
        self.team = team
        super().__init__(name,age,height,weight)
    #override
    def eat(self):
        print('Vegetables')
    def exercise(self):
        print('Doing GYM')
    
    #overloading
    # "+" overload
    def __add__(self,other):
        return self.age + other.age
    #"*" overload
    def __mul__(self,other):
        return self.weight + other.weight
    # "len" overload
    def __len__(self):
        return self.height
    # ">" overload
    def __gt__(self,other):
        return self.age > other.age

Tamim = cricketer('tamim',38,68,91,'BD')
Mushfiq = cricketer('mushfiq',33,60,78,'BD')
Tamim.eat()
Tamim.exercise()

# overload

#plus sign overload
print(1+2)
print('One'+'Five')
print([12,98]+[5,6,7,1,2])
print(Tamim + Mushfiq)
print(Tamim * Mushfiq)
print(len(Tamim))
print(len(Mushfiq))
print(Tamim>Mushfiq)
