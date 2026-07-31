class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100;
        self.max_withdraw = 100000;

    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
    def withdraw(self,amount):
        if amount < self.min_withdraw :
            print(f'You Can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'Your Balance: {self.balance}')
            print(f'Your Balance: {self.get_balance()}')
        
Brac = Bank(15000)
Brac.withdraw(25)
Brac.withdraw(500000) 
Brac.withdraw(1000)
