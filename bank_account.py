# ================================
# Bank Account — Complete System
# ================================
# Built across 6 topics:
# 01 — class, __init__, instance methods
# 02 — class variables, interest_rate, account_count
# 03 — @classmethod from_string(), @staticmethod is_valid_amount()
# 04 — SavingsAccount, CurrentAccount subclasses, super(), overdraft
# 05 — __str__, __repr__, __add__, __eq__, __gt__, __lt__
# 06 — @property balance with validation, getter, setter, deleter
# ================================


class BankAccount:

    interest_rate = 0.03
    account_count = 0

    def __init__(self, owner, balance=0):
        self.owner    = owner
        self._balance = balance   # _balance = "private" — access via property
        BankAccount.account_count += 1

    # --- Property: balance ---

    @property
    def balance(self):
        # Accessed like acc.balance — not acc.balance()
        return self._balance

    @balance.setter
    def balance(self, amount):
        # Runs when you do acc.balance = 5000
        # Validates before setting
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a number.")
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    @balance.deleter
    def balance(self):
        # Runs when you do: del acc.balance
        print(f"  ~ Resetting {self.owner}'s balance to 0.")
        self._balance = 0

    # --- Regular methods ---

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
        self.balance += amount   # triggers balance.setter
        print(f"  + Deposited Rs.{amount} — New balance: Rs.{self.balance:.2f}")

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("  ! Invalid withdraw amount.")
            return
        if amount > self.balance:
            print(f"  ! Insufficient funds. Balance: Rs.{self.balance:.2f}")
            return
        self.balance -= amount   # triggers balance.setter
        print(f"  - Withdrew Rs.{amount} — New balance: Rs.{self.balance:.2f}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"  ~ Interest Rs.{interest:.2f} applied — New balance: Rs.{self.balance:.2f}")

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

    def __str__(self):
        return f"{self.owner}'s account — Balance: Rs.{self.balance:.2f}"

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance


# ================================
# SavingsAccount
# ================================

class SavingsAccount(BankAccount):
    interest_rate = 0.06

    def __repr__(self):
        return f"SavingsAccount('{self.owner}', {self.balance})"

    def __str__(self):
        return f"{self.owner}'s savings — Balance: Rs.{self.balance:.2f} | Rate: 6%"


# ================================
# CurrentAccount
# ================================

class CurrentAccount(BankAccount):
    interest_rate = 0.01

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
        self._balance -= amount   # bypass setter — overdraft is allowed
        print(f"  - Withdrew Rs.{amount} — Balance: Rs.{self.balance:.2f}")

    def __repr__(self):
        return f"CurrentAccount('{self.owner}', {self.balance}, overdraft_limit={self.overdraft_limit})"

    def __str__(self):
        return f"{self.owner}'s current — Balance: Rs.{self.balance:.2f} | Overdraft: Rs.{self.overdraft_limit}"


# ================================
# TEST — Complete system
# ================================

# Create accounts
acc     = BankAccount("Kamal", 10000)
savings = SavingsAccount("Nimal", 50000)
current = CurrentAccount("Amal", 5000, overdraft_limit=15000)

print(f"Total accounts: {BankAccount.account_count}")

# @property — access like attribute
print(f"\nBalance: Rs.{acc.balance}")   # no parentheses needed

# deposit and withdraw — triggers setter internally
acc.deposit(5000)
acc.withdraw(2000)

# apply interest
savings.apply_interest()   # 6%
current.apply_interest()   # 1%

print()
print(acc)
print(savings)
print(current)

# Dunder operations
print(f"\nKamal + Nimal combined: Rs.{acc + savings:.2f}")
print(f"Kamal > Nimal: {acc > savings}")

# Sort accounts
accounts = [current, acc, savings]
accounts.sort(key=lambda a: a.balance)
print("\nAccounts sorted by balance:")
for a in accounts:
    print(f"  {a}")

# balance setter — validation
try:
    acc.balance = -500   # raises ValueError
except ValueError as e:
    print(f"\n  ! Error: {e}")

# balance deleter — resets to 0
del acc.balance
print(acc)

# from_string constructor
acc4 = BankAccount.from_string("Sunil:25000")
print(f"\n{acc4}")
print(f"Total accounts: {BankAccount.account_count}")
