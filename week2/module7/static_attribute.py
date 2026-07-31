class shopping:
    cart = [] #class attribute/static attribute
    origin = 'china'
    def __init__(self):
        pass

    def __init__(self,name,location):
        self.name = 'Jamuna Future Park' #instance attribute
        self.location = "Bashundhara"

    
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'Buying: {item} for price: {price} and remaining: {remaining}')
    
    @classmethod
    def buying(self,item):
        print("Buy what you want")

    @staticmethod
    def multiply(a,b):
        result = a*b
        print(result)

Jamuna = shopping("jamuna",'Kuril')
Jamuna.purchase("Shirt",500,1000)
shopping.purchase('a',2,3,3)

Jamuna.buying('shirt')
shopping.buying('shirt')

shopping.multiply(4,6)
Jamuna.multiply(4,6)

#static method vs class method