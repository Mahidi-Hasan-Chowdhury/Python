def call():
    print('Calling Someone i don\'t know')
class phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    feature = ['camera','speaker']

    def call(self):
        print('Call 1 person')
    def sms(self,phone,sms):
        text = f'sending sms: {phone} and message: {sms}'
        return text

my_phone = phone()
print(my_phone.feature)
my_phone.call()
result = my_phone.sms(1234,'I love python')
print(result) 