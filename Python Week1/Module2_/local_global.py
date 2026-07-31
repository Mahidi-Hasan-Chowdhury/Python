balance = 3000

def buy_things(item,price):
    #you can access global variable without using the global 
    #if you want to modify a global variable,you have to use the global keyword.
    global balance
    print(f'balance before buying',balance)
    balance = balance - price
    print(f'balance after buying {item}', balance)
buy_things('sunglass',1000) 