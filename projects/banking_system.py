class Account:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self._account_number = account_number
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount

    def __str__(self):
        return f"Account {self._account_number} ({self.owner}): Balance ${self._balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, account_number: str, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest

class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        self.accounts[account._account_number] = account

    def get_account(self, account_number: str):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found!")
        return account

    def transfer(self, from_acct: str, to_acct: str, amount: float):
        source = self.get_account(from_acct)
        target = self.get_account(to_acct)
        source.withdraw(amount)
        target.deposit(amount)
