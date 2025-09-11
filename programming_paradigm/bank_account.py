class BankAccount:
    def __init__(self, initial_balance=0.0):
        
        self._balance = float(initial_balance)

    def deposit(self, amount):
        
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        
        amount = float(amount)
        if amount <= 0:
            return False
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        
        print(f"Current Balance: ${self._balance:.2f}")
