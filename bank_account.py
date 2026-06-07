# ================================
# Topic 02 — Bank Account
# ================================
# New concepts: class variables, employee_count pattern
# Added: interest_rate (shared), account_count (tracks total)
# ================================


class BankAccount:

    interest_rate  = 0.03   # class variable — same for all accounts
    account_count  = 0      # class variable — tracks total accounts created

    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
        BankAccount.account_count += 1   # increment every time a new account is created

    def deposit(self, amount):
        if amount <= 0:
            print("  ! Amount must be greater than 0.")
            return
        self.balance += amount
        print(f"  + Deposited Rs.{amount} — New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("  ! Amount must be greater than 0.")
            return
        if amount > self.balance:
            print(f"  ! Insufficient funds. Balance: Rs.{self.balance}")
            return
        self.balance -= amount
        print(f"  - Withdrew Rs.{amount} — New balance: Rs.{self.balance}")

    def apply_interest(self):
        # Uses self.interest_rate — checks instance first, then class
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"  ~ Interest applied: Rs.{interest:.2f} — New balance: Rs.{self.balance:.2f}")

    def info(self):
        return f"Owner: {self.owner} | Balance: Rs.{self.balance:.2f} | Rate: {self.interest_rate * 100}%"


# ================================
# TEST
# ================================

acc1 = BankAccount("Kamal", 10000)
acc2 = BankAccount("Nimal", 20000)

print(f"Total accounts: {BankAccount.account_count}")   # 2

acc1.apply_interest()   # 3% on 10000 → Rs.300
acc2.apply_interest()   # 3% on 20000 → Rs.600

print(acc1.info())
print(acc2.info())

# Give acc1 a personal interest rate — doesn't affect acc2
acc1.interest_rate = 0.05
acc1.apply_interest()   # 5%
acc2.apply_interest()   # still 3%

print(acc1.info())
print(acc2.info())

# Update rate for everyone via the class
BankAccount.interest_rate = 0.04
print(f"\nNew global rate: {BankAccount.interest_rate}")
print(f"acc1 rate: {acc1.interest_rate}")   # still 0.05 — has its own
print(f"acc2 rate: {acc2.interest_rate}")   # 0.04 — uses class rate
