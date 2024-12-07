class BankAccount:
    def __init__(self, account_holder_name: str, balance: float):
        self.account_holder_name = account_holder_name
        # This "_" in front represents that the attribute is not to be accessed directly from the outside
        # There are helper functions to change or view the balance
        self._balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance:.2f}")
        else: print("Error: Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. New balance is {self._balance:.2f}")
            else: print("Error: Insufficient funds.")
        else: print("Error: Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance



account = BankAccount("Alice", 1000.0)

print(f"Account Holder: {account.account_holder_name}")
print(f"Initial Balance: {account.get_balance()}")

account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(2000.0)
