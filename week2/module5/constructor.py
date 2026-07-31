class phone:
    manufacturer = 'china'
    
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sms(self,phone,sms):
        text = f'sending sms: {phone} and message: {sms}'
        print(text)

my_phone = phone('Mahidi','Infinix','7000')
her_phone = phone('she','Apple','100000')
print(my_phone.owner,my_phone.brand,my_phone.price)
print(her_phone.owner,her_phone.brand,her_phone.price)
my_phone.sms(123,'hello')
her_phone.sms(345,'hi')
