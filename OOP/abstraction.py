from abc import ABC, abstractmethod
class Enforce(ABC):
    @abstractmethod
    def EngineStart(self):
        pass


class Bike(Enforce):
    def EngineStart(self):
        print("Bike engine started.")

class Car(Enforce):
    def EngineStart(self):
        print("Car engine started.")
class Truck(Enforce):
    def EngineStart(self):
        print("Truck engine started.")


obj1 = Bike().EngineStart()
obj2 = Car().EngineStart()
obj3 = Truck().EngineStart()

