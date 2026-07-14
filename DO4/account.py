class Account():
    def __init__(self, owner, account_number, balance=0):
        self._balance = balance
        self.owner = owner
        self.account_number = account_number

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
    


# Create an account
almaz = Account("Almaz Bekele", "CBE-1001", 1500)

# Test deposit
almaz.deposit(500)
print(almaz.balance) 

# Test withdrawal
almaz.withdraw(300)
print(almaz.balance)  

# Test statement
print(almaz.statement())
