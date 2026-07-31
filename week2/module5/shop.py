class shop:
    cart = [] #cart is a class attribute
    def __init__(self,buyer):
       self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)

mahidi = shop('Mahidi Hasan')
mahidi.add_to_cart('shoes')
mahidi.add_to_cart('phone')
print(mahidi.cart)

siam = shop("siam")
siam.add_to_cart('cap')
siam.add_to_cart('watch')
print(siam.cart)