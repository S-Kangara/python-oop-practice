# ================================
# Topic 05 — Bank Account
# ================================
# New concepts: __repr__, __str__, __add__, __eq__, __gt__
# ================================


class BankAccount:

    interest_rate = 0.03
    account_count = 0

    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
        BankAccount.account_count += 1

    @classmethod
    def from_string(cls, account_str):
        owner, balance = account_str.split(':')
        return cls(owner, int(balance))

    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            print("  ! Invalid deposit amount.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("  ! Invalid withdraw amount.")
            return
        if amount > self.balance:
            print(f"  ! Insufficient funds. Balance: Rs.{self.balance:.2f}")
            return
        self.balance -= amount

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    # --- Dunder methods ---

    def __repr__(self):
        # For developers — recreates the object
        return f"BankAccount('{self.owner}', {self.balance})"

    def __str__(self):
        # For users — readable summary
        return f"{self.owner}'s account — Balance: Rs.{self.balance:.2f}"

    def __add__(self, other):
        # acc1 + acc2 → combined balance (returns a number)
        return self.balance + other.balance

    def __eq__(self, other):
        # acc1 == acc2 → same owner and balance?
        return self.owner == other.owner and self.balance == other.balance

    def __gt__(self, other):
        # acc1 > acc2 → higher balance?
        return self.balance > other.balance

    def __lt__(self, other):
        # acc1 < acc2 → lower balance?
        return self.balance < other.balance


class SavingsAccount(BankAccount):
    interest_rate = 0.06

    def __repr__(self):
        return f"SavingsAccount('{self.owner}', {self.balance})"

    def __str__(self):
        return f"{self.owner}'s savings account — Balance: Rs.{self.balance:.2f} | Rate: 6%"


class CurrentAccount(BankAccount):
    interest_rate   = 0.01
    overdraft_limit = 10000

    def __init__(self, owner, balance=0, overdraft_limit=10000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("  ! Invalid withdraw amount.")
            return
        if amount > self.balance + self.overdraft_limit:
            print(f"  ! Exceeds overdraft limit.")
            return
        self.balance -= amount

    def __repr__(self):
        return f"CurrentAccount('{self.owner}', {self.balance}, overdraft_limit={self.overdraft_limit})"

    def __str__(self):
        return f"{self.owner}'s current account — Balance: Rs.{self.balance:.2f} | Overdraft: Rs.{self.overdraft_limit}"


# ================================
# TEST
# ================================

acc1    = BankAccount("Kamal", 50000)
acc2    = BankAccount("Nimal", 30000)
savings = SavingsAccount("Amal", 50000)

# __repr__ and __str__
print(repr(acc1))     # BankAccount('Kamal', 50000)
print(str(acc1))      # Kamal's account — Balance: Rs.50000.00
print(acc1)           # same as str — uses __str__

print(repr(savings))
print(savings)

# __add__
total = acc1 + acc2
print(f"\nCombined balance: Rs.{total}")   # 80000

# __eq__
acc3 = BankAccount("Kamal", 50000)
print(acc1 == acc3)   # True — same owner and balance
print(acc1 == acc2)   # False

# __gt__ and __lt__
print(acc1 > acc2)    # True  — 50000 > 30000
print(acc2 < acc1)    # True

# Sort a list of accounts by balance using dunders
accounts = [acc2, acc1, savings]
accounts.sort(key=lambda a: a.balance)
for a in accounts:
    print(a)
