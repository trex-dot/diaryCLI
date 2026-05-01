class BankAccount:
    def __init__(self,name,balance,):
        self.name=name
        self.balance=balance
        self.transactionHistory=[]
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if value<0:
            raise ValueError("InsufficientFundsError") 
        self._balance=value
    def deposit(self,amount):
        self.balance=self.balance+amount
        self.transactionHistory.append(f"Deposit: {amount}")
    def withdraw(self,amount):
        if (self.balance-amount)<0:
            raise InsufficientFundsError('Not enough funds')
        self.balance=self.balance-amount
        self.transactionHistory.append(f"Withdrawal: {amount}")

    def __str__(self):
         return f"Account({self.name}, Balance: {self.balance})"    

class InsufficientFundsError(Exception):
    pass       

class SavingsAccount(BankAccount):
    def __init__(self,name,balance,interest_rate):
            super().__init__(name,balance)
            
            self.interest_rate=interest_rate
    def apply_interest(self):
            self.balance = self.balance + (self.balance * self.interest_rate/100)


acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)
print(acc.transactionHistory)

savings = SavingsAccount("Sara", 2000, 5)
savings.apply_interest()
print(savings)

try:
    acc.withdraw(5000)
except InsufficientFundsError:
    print("Error: Not enough funds")