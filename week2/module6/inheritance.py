class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Gadget: {self.brand}'
    
class laptop:
    def __init__(self,memory,ssd):
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'Learning Python'

class phone(Gadget): 
    def __init__(self,brand,price,color,origin,dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)
    def phone_call(self,number,text):
        return f'Sending SMS to: {number} with: {text}'
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price}  {self.dual_sim}'

class camera:
    def __init__(self,pixel):
        self.pixel = pixel
    def change_lens(self):
        pass 

my_phone = phone('IPhone',120000,'Gold','China',True)
print(my_phone.brand)
print(my_phone)