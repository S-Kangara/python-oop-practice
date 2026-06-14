# Topic 04 — Inheritance & Subclasses

## What is Inheritance?
- A subclass **inherits** all methods and attributes from a parent class
- Lets you reuse code without repeating it
- You can add new behaviour or override existing behaviour

```python
class Developer(Employee):   # Developer inherits from Employee
    pass
```

## The `super()` Function
- Calls the parent class's `__init__` — handles shared attributes
- Keeps code DRY (Don't Repeat Yourself)

```python
class Developer(Employee):
    def __init__(self, name, pay, prog_lang):
        super().__init__(name, pay)   # parent handles name and pay
        self.prog_lang = prog_lang    # Developer-specific
```

## Method Resolution Order (MRO)
- The chain Python follows when looking for a method or attribute
- Checks subclass first, then moves up the inheritance tree
- View it with `ClassName.__mro__` or `help(ClassName)`

## Overriding Methods
- Define a method with the same name in the subclass
- Python uses the subclass version first

## Useful Built-in Functions
```python
isinstance(dev, Developer)    # True — is dev an instance of Developer?
isinstance(dev, Employee)     # True — also an instance of Employee
issubclass(Developer, Employee)  # True — Developer inherits from Employee
```

## Key Point
A subclass instance is also an instance of every class above it
in the inheritance chain. `isinstance` reflects this.
