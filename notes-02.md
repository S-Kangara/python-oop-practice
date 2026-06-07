# Topic 02 — Class Variables vs Instance Variables

## Instance Variables
- Data that is **unique to each object**
- Defined inside `__init__` using `self`
- Example: `self.name`, `self.email`, `self.pay`

## Class Variables
- Data that is **shared across all instances**
- Defined directly inside the class body (not inside any method)
- Example: a company-wide raise amount

```python
class Employee:
    raise_amount = 1.05  # class variable — shared by all
```

## Attribute Lookup Order
1. Python checks the **instance** namespace first
2. If not found, checks the **class** namespace
3. This is why `self.raise_amount` works even without setting it on the instance

## Modifying Variables
```python
Employee.raise_amount = 1.10   # updates for ALL instances
emp1.raise_amount = 1.20       # creates a new attribute on emp1 only
```

## Key Rule
- Use instance variables for data that differs per object
- Use class variables for data that should be the same for every object

## Common Mistake
Setting a class variable via an instance creates a new instance variable
instead of modifying the class variable. Always update class variables
through the class itself.
