class Account:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self._account_number = account_number
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        amount = abs(amount)
        self._balance += amount

    def withdraw(self, amount: float):
        amount = abs(amount)
        self._balance -= amount

    def __str__(self):
        return f"Account {self._account_number} ({self.owner}): Balance ${self._balance:.2f}"

class SavingsAccount(Account):
    pass

class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def transfer(self, from_acct: str, to_acct: str, amount: float):
        pass
