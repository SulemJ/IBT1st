from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, owner, account_number, balance=0):
        self._balance = balance
        self.owner = owner
        self.account_number = account_number
    @abstractmethod
    def calculate_interest(self):
        pass

    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "insuffincient funds"
    def statement(self):
        return f"{self.owner} has {self.balance} ETB in their account"
    


class SavingsAccount(Account):
    def __init__(self, owner, account_number, rate, balance=0):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def statement(self):
        return f"{self.owner} has {self.balance} ETB in their saving account"
    
    def calculate_interest(self):
        return self._balance * self.rate  
    
    def add_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
        return self._balance

class CurrentAccount(Account):
    def __init__(self, owner, account_number, overdraft=1000, balance=0):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def statement(self):
        return f"{self.owner} has {self.balance} ETB in their current account"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance + self.overdraft:
            raise ValueError(f"Overdraft limit exceeded. Available: {self._balance + self.overdraft}")
        self._balance -= amount
        return self._balance
    
    def calculate_interest(self):
        return 0


accounts = [
    SavingsAccount("Almaz", "CBE-1", 0.05, 1500),
    CurrentAccount("Dawit", "CBE-2", 1000, 800),
]

for acc in accounts:
    acc.deposit(100)
    print(acc.statement())
    if isinstance(acc, SavingsAccount):
        acc.add_interest()
        print(f"After interest: {acc.balance}")