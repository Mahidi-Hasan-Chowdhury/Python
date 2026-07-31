#inheritance provides you "is" a relation
class animal:
    pass
class Dog(animal):
    pass

#class is a animal
class Tiger(animal):
    pass


class furniture:
    pass
#chair is a furniture
class chair(furniture):
    pass
class bed(furniture):
    pass

#composition

class engine:
    def __init__(self):
        pass
    def start(self):
        return"Engine Started"
    
class driver:
    def __init__(self):
        pass
    
#car has an engine

class car:
    def __init__(self):
        self.engine = engine()
        self.driver = driver()

    def start(self):
        self.engine.start()



class cpu:
    def __init__(self,cores):
        self.cores = cores

class ram:
    def __init__(self,size):
        self.size = size

class HardDrive:
    def __init__(self,capacity):
        self.capacity = capacity

class computer:
    def __init__(self,cores,ram_size,hd_capacity):
        self.cpu = cpu(cores)
        self.ram = ram(ram_size)
        self.hard_disc = HardDrive(hd_capacity)

mac = computer(12,8,520)
