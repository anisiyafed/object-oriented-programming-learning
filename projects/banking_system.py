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
    def __init__(self, account_number: str, owner: str, balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Insufficient funds! This withdrawal exceeds the overdraft limit.")
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    def __str__(self):
        return (f"Checking Account {self._account_number} ({self.owner}): "
                f"Balance ${self._balance:.2f}, Overdraft Limit ${self.overdraft_limit:.2f}")


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
