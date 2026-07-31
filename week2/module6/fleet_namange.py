class Company:
    def __init__(self,name,address)->None:
        self.name = name 
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []

class driver:
    def __init__(self,name,license,age)->None:
        self.license = license
        self.name = name
        self.age = age
class Counter:
    def __init__(self):
        pass
    def purchase_ticket(self,start,destination):
        pass
class passenger:
    pass
class supervisor:
    pass

driver1 = driver('a',123,25)