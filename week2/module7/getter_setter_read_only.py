class user:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money
    
    #Getter without any setter is read only
    @property #decorator #make this method an attribute
    def age(self):
        return self._age
    # Getter --> Get a value of a property through a method. Most of the time, you will get the value of a private attribute.
    @property
    def salary(self):
        return self.__money
    #setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.
    @salary.setter
    def salary(self,value):
        self.__money += value

mahidi = user('mahidi',21,100)
#print(mahidi.__money)
#print(mahidi.age())
print(mahidi.age)

mahidi.salary = 4500
print(mahidi.salary)
print(mahidi._user__money) # Not recommended but works
