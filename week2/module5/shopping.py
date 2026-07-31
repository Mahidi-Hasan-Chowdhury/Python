class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add_to_cart(self,item,price,quantity):
        product = {'item': item,'price': price,'quantity': quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
        print('total price',total)
        if amount < total:
            return f'Please Provide {total-amount} more '
        else:
            extra = amount - total
            print(f'Here is Your items and Extra money {extra}')
        #def remove_item(self,item): Homework
mahidi = shopping('mahidi hasan')
mahidi.add_to_cart('Egg',10,4)
mahidi.add_to_cart('rice',60,5)
mahidi.add_to_cart('Potato',30,2)

print(mahidi.cart)
mahidi.checkout(600)