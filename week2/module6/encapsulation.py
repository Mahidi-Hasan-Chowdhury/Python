class bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name
        self._branch = 'Rampura'
        self.__balance = initial_deposit

    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'Not Enough Balance'

mahidi = bank('Mahidi',10000)

print(mahidi.holder_name)
mahidi.holder_name = 'siam'
print(mahidi.holder_name)
mahidi.deposit(10000)
print(mahidi.get_balance())
print(mahidi._bank__balance)
#print(dir(mahidi))
print(mahidi._branch)
