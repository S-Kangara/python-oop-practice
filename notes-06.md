# Topic 06 — Property Decorators

## The Problem
If `email` depends on `first` and `last`, and someone changes `first`,
the email doesn't update automatically unless you use a property.

## `@property` — Getter
- Lets you access a method **like an attribute** (no parentheses)
- Existing code doesn't break when you add logic later

```python
@property
def email(self):
    return f"{self.first}.{self.last}@company.com"

emp.email   # accessed like an attribute, not emp.email()
```

## `@name.setter`
- Runs when you **assign** a value to the property
- Lets you add validation or parsing logic

```python
@fullname.setter
def fullname(self, name):
    first, last = name.split(' ')
    self.first = first
    self.last  = last

emp.fullname = "Kamal Perera"   # triggers the setter
```

## `@name.deleter`
- Runs when you **delete** the property
- Used for cleanup logic

```python
@fullname.deleter
def fullname(self):
    self.first = None
    self.last  = None

del emp.fullname   # triggers the deleter
```

## When to Use Properties
- When an attribute's value depends on other attributes
- When you want to add validation without breaking the public interface
- When you need to run code on get, set, or delete

## Key Point
Properties let you start with simple attributes and add logic later
without changing how the rest of your code accesses them.
