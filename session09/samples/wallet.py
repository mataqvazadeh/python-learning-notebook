class Wallet:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            print('Balance is not enough')
            return
        
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print('Wrong')
        else:
            self._balance = amount