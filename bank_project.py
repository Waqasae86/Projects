# Create abstract parent class of account
class Account:
     def __int__(self, name, balance, min_balance):
         self.name = name
         self.balance = balance
         self.min_balamce = min_balance

# instead of repeating self.balance = self.balance + amount, we can use
     def deposit(self, amount):
        self.balance += amount

     def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Balance is too less to withdraw")

     def statement(self):
         print("Account Balance: {} Pounds".format(self.balance))

# now we create our current account, which will adopt traits from the parent account

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000 )

w = Current("Waqas", 500)





