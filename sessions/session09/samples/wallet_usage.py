from wallet import Wallet

my_wallet = Wallet()
print(my_wallet.balance)
my_wallet.withdraw(10)
my_wallet.deposit(10000)
print(my_wallet.balance)
my_wallet.withdraw(10)
print(my_wallet.balance)
my_wallet.withdraw(10000)
my_wallet.balance = -10

