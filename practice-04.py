# ================================
# Topic 04: Inheritance & Subclasses
# ================================

class Employee:
    raise_amount = 1.05

    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __str__(self):
        return f"{self.name} — Rs.{self.pay}"


class Developer(Employee):
    raise_amount = 1.10   # override class variable for developers

    def __init__(self, name, pay, prog_lang):
        super().__init__(name, pay)
        self.prog_lang = prog_lang

    def info(self):
        return f"{self.name} | {self.prog_lang} | Rs.{self.pay}"


class Manager(Employee):
    def __init__(self, name, pay, employees=None):
        super().__init__(name, pay)
        self.employees = employees or []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        for e in self.employees:
            print(f"  - {e.name}")


# ----- TEST -----
dev1 = Developer("Amal", 70000, "Python")
dev2 = Developer("Bimal", 80000, "JavaScript")
mgr  = Manager("Sunil", 100000, [dev1])

print(dev1.info())

dev1.apply_raise()
print(dev1.info())   # 10% raise (Developer raise_amount)

mgr.add_employee(dev2)
mgr.list_employees()

print(isinstance(dev1, Developer))   # True
print(isinstance(dev1, Employee))    # True
print(issubclass(Developer, Employee))  # True


# ----- CHALLENGE -----
# Extend your BankAccount:
# SavingsAccount(BankAccount) — higher interest_rate = 0.05
# CurrentAccount(BankAccount) — overdraft_limit = 10000
# withdraw() can go negative up to overdraft_limit
# TODO: Write it yourself!

class SavingsAccount(BankAccount):
    interest_rate = 0.05

    def __init__(self, owner, balance =0):
        super().__init__(owner, balance)

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
