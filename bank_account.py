# ================================
# Topic 04 — Bank Account
# ================================
# New concepts: inheritance, super(), method overriding
# Added: SavingsAccount, CurrentAccount subclasses
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
        print(f"  + Deposited Rs.{amount} — New balance: Rs.{self.balance:.2f}")

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("  ! Invalid withdraw amount.")
            return
        if amount > self.balance:
            print(f"  ! Insufficient funds. Balance: Rs.{self.balance:.2f}")
            return
        self.balance -= amount
        print(f"  - Withdrew Rs.{amount} — New balance: Rs.{self.balance:.2f}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"  ~ Interest Rs.{interest:.2f} applied — New balance: Rs.{self.balance:.2f}")

    def info(self):
        return f"[{self.__class__.__name__}] Owner: {self.owner} | Balance: Rs.{self.balance:.2f}"


# ================================
# SavingsAccount — higher interest, no overdraft
# ================================

class SavingsAccount(BankAccount):

    interest_rate = 0.06   # higher rate than base BankAccount

    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)   # parent handles owner, balance, account_count


# ================================
# CurrentAccount — lower interest, allows overdraft
# ================================

class CurrentAccount(BankAccount):

    interest_rate   = 0.01
    overdraft_limit = 10000   # can go negative up to this limit

    def __init__(self, owner, balance=0, overdraft_limit=10000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Override withdraw — allows going negative up to overdraft_limit
        if not self.is_valid_amount(amount):
            print("  ! Invalid withdraw amount.")
            return
        if amount > self.balance + self.overdraft_limit:
            print(f"  ! Exceeds overdraft limit. Max withdraw: Rs.{self.balance + self.overdraft_limit:.2f}")
            return
        self.balance -= amount
        if self.balance < 0:
            print(f"  - Withdrew Rs.{amount} — Overdraft: Rs.{self.balance:.2f}")
        else:
            print(f"  - Withdrew Rs.{amount} — New balance: Rs.{self.balance:.2f}")


# ================================
# TEST
# ================================

savings  = SavingsAccount("Kamal", 50000)
current  = CurrentAccount("Nimal", 10000)
base_acc = BankAccount("Amal", 10000)

print(f"Total accounts: {BankAccount.account_count}")   # 3

# Different interest rates
savings.apply_interest()    # 6%
current.apply_interest()    # 1%
base_acc.apply_interest()   # 3%

print(savings.info())
print(current.info())
print(base_acc.info())

# CurrentAccount overdraft
current.withdraw(15000)   # goes into overdraft
print(current.info())
current.withdraw(6000)    # exceeds overdraft limit — rejected

# isinstance checks
print(isinstance(savings, SavingsAccount))   # True
print(isinstance(savings, BankAccount))      # True — inherits
print(issubclass(SavingsAccount, BankAccount))  # True
