# ================================
# Topic 03: Class Methods & Static Methods
# ================================

import datetime

class Employee:
    raise_amount = 1.05

    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    # Regular method — uses self
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class method — alternative constructor
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # "Kamal-50000" → Employee("Kamal", 50000)
        name, pay = emp_str.split('-')
        return cls(name, int(pay))

    # Static method — utility, no self or cls needed
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5   # Mon=0, Sun=6


# ----- TEST -----
emp1 = Employee("Kamal", 50000)
emp2 = Employee.from_string("Nimal-60000")   # classmethod

print(emp2.name)   # Nimal
print(emp2.pay)    # 60000

Employee.set_raise_amount(1.10)
emp1.apply_raise()
print(emp1.pay)    # 55000

my_date = datetime.date(2025, 6, 2)   # Monday
print(Employee.is_workday(my_date))   # True


# ----- CHALLENGE -----
# Add to your BankAccount class from topic 02:
# @classmethod  from_string(cls, s) — "owner:balance" → BankAccount
# @staticmethod is_valid_amount(amount) → True if amount > 0
# TODO: Write it yourself!
