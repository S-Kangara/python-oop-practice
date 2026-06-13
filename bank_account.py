# ================================
# Topic 03 — Bank Account
# ================================
# New concepts: @classmethod, @staticmethod
# Added: from_string() constructor, is_valid_amount() utility
# ================================


class BankAccount:

    interest_rate = 0.03
    account_count = 0

    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
        BankAccount.account_count += 1

    # --- Alternative constructor ---
    # Creates a BankAccount from a string like "Kamal:5000"
    @classmethod
    def from_string(cls, account_str):
        owner, balance = account_str.split(':')
        return cls(owner, int(balance))

    # --- Class-level rate update ---
    # Updates interest rate for all accounts
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        print(f"  ~ Interest rate updated to {rate * 100}%")

    # --- Utility function ---
    # Checks if an amount is valid — doesn't need self or cls
    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def deposit(self, amount):
        if not BankAccount.is_valid_amount(amount):
            print("  ! Invalid deposit amount.")
            return
        self.balance += amount
        print(f"  + Deposited Rs.{amount} — New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            print("  ! Invalid withdraw amount.")
            return
        if amount > self.balance:
            print(f"  ! Insufficient funds. Balance: Rs.{self.balance}")
            return
        self.balance -= amount
        print(f"  - Withdrew Rs.{amount} — New balance: Rs.{self.balance}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"  ~ Interest applied: Rs.{interest:.2f} — New balance: Rs.{self.balance:.2f}")

    def info(self):
        return f"Owner: {self.owner} | Balance: Rs.{self.balance:.2f}"


# ================================
# TEST
# ================================

# Normal constructor
acc1 = BankAccount("Kamal", 10000)

# Alternative constructor — from a string
acc2 = BankAccount.from_string("Nimal:20000")
acc3 = BankAccount.from_string("Amal:5000")

print(f"Total accounts: {BankAccount.account_count}")   # 3
print(acc2.info())   # Owner: Nimal | Balance: Rs.20000

# Static method — validate before doing anything
print(BankAccount.is_valid_amount(500))    # True
print(BankAccount.is_valid_amount(-100))   # False
print(BankAccount.is_valid_amount("abc"))  # False

acc1.deposit(5000)
acc1.deposit(-50)    # rejected by is_valid_amount

# Update rate for all accounts
BankAccount.set_interest_rate(0.05)
acc1.apply_interest()
acc2.apply_interest()

print(acc1.info())
print(acc2.info())
