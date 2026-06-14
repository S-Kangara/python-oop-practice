# ================================
# Topic 05: Special (Dunder) Methods
# ================================

class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    def __repr__(self):
        # For developers — should recreate the object
        return f"Employee('{self.name}', {self.pay})"

    def __str__(self):
        # For users — readable
        return f"{self.name} — Rs.{self.pay}"

    def __add__(self, other):
        # emp1 + emp2 → combined pay
        return self.pay + other.pay

    def __len__(self):
        # len(emp) → length of name
        return len(self.name)

    def __eq__(self, other):
        # emp1 == emp2 → same name and pay?
        return self.name == other.name and self.pay == other.pay


# ----- TEST -----
emp1 = Employee("Kamal", 50000)
emp2 = Employee("Nimal", 60000)
emp3 = Employee("Kamal", 50000)

print(repr(emp1))      # Employee('Kamal', 50000)
print(str(emp1))       # Kamal — Rs.50000
print(emp1)            # Kamal — Rs.50000  (uses __str__)

print(emp1 + emp2)     # 110000
print(len(emp1))       # 5

print(emp1 == emp2)    # False
print(emp1 == emp3)    # True


# ----- CHALLENGE -----
# Add to BankAccount:
# __repr__ → "BankAccount('owner', balance)"
# __str__  → "owner's account — balance: Rs.X"
# __add__  → combine two accounts' balances
# __gt__   → account1 > account2 based on balance
# TODO: Write it yourself!

# ****** I used these Dunder methods in bank_account.py ******
