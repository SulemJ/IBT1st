from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, account_number, balance=0):
        self._balance = balance
        self.owner = owner
        self.account_number = account_number
        self._observers = []
        self.history = []
    
    @abstractmethod
    def calculate_interest(self):
        pass
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self.history.append(f"+{amount} ETB")
        self._notify(f"+{amount} ETB")
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.history.append(f"-{amount} ETB")
        self._notify(f"-{amount} ETB")
        return self._balance
    
    def statement(self):
        return f"{self.owner} has {self.balance} ETB in their account"
    
    def subscribe(self, obs):
        self._observers.append(obs)
    
    def _notify(self, event):
        for obs in self._observers:
            obs.update(event)
    
    def undo_last(self):
        if not self.history:
            return None
        last = self.history.pop()
        amount = int(last.split()[0][1:])
        if last.startswith("+"):
            self._balance -= amount
            return f"Undid deposit of {amount} ETB"
        else:
            self._balance += amount
            return f"Undid withdrawal of {amount} ETB"
    
    def total_transactions(self):
        if not self.history:
            return 0
        amount = int(self.history[0].split()[0][1:])
        return amount + self.total_transactions_helper(1)
    
    def total_transactions_helper(self, index):
        if index >= len(self.history):
            return 0
        amount = int(self.history[index].split()[0][1:])
        return amount + self.total_transactions_helper(index + 1)


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


class OverdraftConfig:
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
        return OverdraftConfig().overdraft
    
    def statement(self):
        return f"{self.owner} has {self.balance} ETB in their current account"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance + self.overdraft:
            raise ValueError(f"Overdraft limit exceeded. Available: {self._balance + self.overdraft}")
        self._balance -= amount
        self.history.append(f"-{amount} ETB")
        self._notify(f"-{amount} ETB")
        return self._balance
    
    def calculate_interest(self):
        return 0


class AccountFactory:
    @staticmethod
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


class AccountRegistry:
    def __init__(self):
        self.by_number = {}
        self.order = []
    
    def add(self, acc):
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)
    
    def find(self, number):
        return self.by_number.get(number)
    
    def list_all(self):
        return [self.by_number[num] for num in self.order]
    
    def total_balance(self):
        total = 0
        for acc in self.list_all():
            total += acc.balance
        return total
    
    def top_by_balance(self, n):
        sorted_accounts = sorted(self.list_all(), key=lambda acc: acc.balance, reverse=True)
        return sorted_accounts[:n]
    
    def binary_search(self, sorted_numbers, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if sorted_numbers[mid] == target:
            return mid
        elif sorted_numbers[mid] < target:
            return self.binary_search(sorted_numbers, target, mid + 1, right)
        else:
            return self.binary_search(sorted_numbers, target, left, mid - 1)
    
    def find_by_number(self, number):
        sorted_numbers = sorted(self.by_number.keys())
        index = self.binary_search(sorted_numbers, number, 0, len(sorted_numbers) - 1)
        if index != -1:
            return self.by_number[sorted_numbers[index]]
        return None


if __name__ == "__main__":
    registry = AccountRegistry()
    
    acc1 = AccountFactory.create("savings", "Almaz", "CBE-1", 1500)
    acc2 = AccountFactory.create("current", "Dawit", "CBE-2", 800)
    acc3 = AccountFactory.create("savings", "Hanna", "CBE-3", 2000)
    acc4 = AccountFactory.create("current", "Yonas", "CBE-4", 500)
    acc5 = AccountFactory.create("savings", "Sara", "CBE-5", 3000)
    
    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)
    registry.add(acc4)
    registry.add(acc5)
    
    print("Top 3 by balance:")
    for acc in registry.top_by_balance(3):
        print(f"  {acc.owner}: {acc.balance} ETB")
    
    found = registry.find_by_number("CBE-3")
    if found:
        print(found.statement())
    
    found = registry.find_by_number("CBE-99")
    if found:
        print(found.statement())
    else:
        print("CBE-99 not found")
    
    acc1.deposit(100)
    acc1.deposit(50)
    acc1.withdraw(30)
    print(f"Total transaction amount for {acc1.owner}: {acc1.total_transactions()} ETB")
    
   