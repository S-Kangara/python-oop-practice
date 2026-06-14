# ================================
# Topic 06: Property Decorators
# ================================

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    @property
    def email(self):
        # Accessed like emp.email — not emp.email()
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        # "Kamal Perera" → first="Kamal", last="Perera"
        first, last  = name.split(' ')
        self.first   = first
        self.last    = last

    @fullname.deleter
    def fullname(self):
        print("Deleting name...")
        self.first = None
        self.last  = None


# ----- TEST -----
emp = Employee("Kamal", "Perera", 50000)

print(emp.email)      # Kamal.Perera@company.com
print(emp.fullname)   # Kamal Perera

emp.first = "Nimal"
print(emp.email)      # Nimal.Perera@company.com  (updates automatically)

emp.fullname = "Amal Silva"
print(emp.first)      # Amal
print(emp.last)       # Silva
print(emp.email)      # Amal.Silva@company.com

del emp.fullname      # Deleting name...


# ----- CHALLENGE -----
# Add to BankAccount:
# @property balance — return self._balance
# @balance.setter   — validate: don't allow negative balance
# @balance.deleter  — reset to 0 with a print message
# Hint: store the actual value in self._balance (convention for "private")
# TODO: Write it yourself!

# ****** I used the Property decorators in bank_account.py ******
