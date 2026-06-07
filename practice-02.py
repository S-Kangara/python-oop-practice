# ================================
# Topic 02: Class vs Instance Variables
# ================================

class Employee:
    # Class variable — shared by all employees
    raise_amount   = 1.05
    employee_count = 0

    def __init__(self, name, pay):
        self.name = name       # instance variable
        self.pay  = pay        # instance variable
        Employee.employee_count += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def info(self):
        return f"{self.name} — Rs.{self.pay}"


# ----- TEST -----
emp1 = Employee("Kamal", 50000)
emp2 = Employee("Nimal", 60000)

print(Employee.employee_count)   # 2

emp1.apply_raise()
print(emp1.info())               # pay increased by 5%

# Update raise for all
Employee.raise_amount = 1.10
emp2.apply_raise()
print(emp2.info())               # pay increased by 10%

# Update raise for emp1 only
emp1.raise_amount = 1.20
emp1.apply_raise()
print(emp1.info())               # emp1 gets 20% raise

# emp2 still uses class raise_amount
print(emp2.raise_amount)         # 1.10


# ----- CHALLENGE -----
# BankAccount class
# Class variable  : interest_rate = 0.03
# Instance vars   : owner, balance
# method: apply_interest() → balance += balance * interest_rate
# method: deposit(amount)
# method: withdraw(amount) — don't allow negative balance
# TODO: Write it yourself!

class BankAccount:
    interest_rate = 0.03  

    def __init__(self, owner, balance):
        self.owner   = owner 
        self.balance = balance  

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate  

    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount):
        if amount > self.balance:    
            print("Insufficient funds")
            return
        self.balance -= amount


# test
acc1 = BankAccount("Kamal", 10000)
print(acc1.balance)       
acc1.deposit(5000)
print(acc1.balance)       
acc1.apply_interest()
print(acc1.balance)       
acc1.withdraw(20000)     
acc1.withdraw(5000)
print(acc1.balance)  
