


from abc import ABC, abstractmethod
class Account(ABC):

    # def __init__(self):
    #     self._observers = []
    # def subscribe(self, obs):
    #     self._observers.append(obs)
    # def _notify(self, event):
    #     for obs in self._observers:
    #         obs.update(event)
    # def withdraw(self, amount):
    #     self.balance -= amount
        


    def __init__(self, owner, account_number, balance=0):
        self._balance = balance
        self.owner = owner
        self.account_number = account_number
        self._observers = []
    @abstractmethod
    def calculate_interest(self):
        pass

    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        self._balance += amount
        self._notify(f"+{amount} ETB")
        return self._balance
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._notify(f"-{amount} ETB")
        return self._balance
    def statement(self):
        return f"{self.owner} has {self.balance} ETB in their account"
    
    def subscribe(self, obs):
        self._observers.append(obs)

    def _notify(self, event):
        for obs in self._observers:
            obs.update(event)
    


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




class overdraftConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.overdraft = 1000
        
        return cls._instance
    
    def set_overdraft(self, new_value):
        self._instance.overdraft = new_value

class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)

    @property
    def overdraft(self):
        
        return overdraftConfig().overdraft

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



config = overdraftConfig()
config.set_overdraft(2000)

# accounts = [
#     SavingsAccount("Almaz", "CBE-1", 0.05, 1500),
#     CurrentAccount("Dawit", "CBE-2", 800),
# ]

# for acc in accounts:
#     acc.deposit(100)
#     print(acc.statement())
#     if isinstance(acc, SavingsAccount):
#         acc.add_interest()
#         print(f"After interest: {acc.balance}")
#     if isinstance(acc, CurrentAccount):
#         # acc.add_interest()
#         print(f"new overdraft is: {acc.overdraft}")


class AccountFactory:

    def create(kind, owner, account_number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, account_number, 0.05, balance)
        if kind == "current":
            return CurrentAccount(owner, account_number, balance)
        raise ValueError(f"Unknown type: {kind}")

class SMSAlert:
 def update(self, event):
    print(f"[send SMS of] {event}")

class AuditLog:
 def update(self, event):
    print(f"[save Log of] {event}")
    
acc = AccountFactory.create("savings", "Almaz", "CBE-1")
# print(acc.owner)



acc.subscribe(SMSAlert())
acc.subscribe(AuditLog())
acc.deposit(500)
acc.withdraw(200)