# Topic 05 — Special (Dunder) Methods

## What are Dunder Methods?
- Methods with double underscores on both sides: `__method__`
- Let you define how objects behave with built-in Python operations
- Also called "magic methods" or "special methods"

## `__repr__`
- Unambiguous representation — meant for **developers and debugging**
- Should return a string that could recreate the object
- Fallback if `__str__` is not defined

```python
def __repr__(self):
    return f"Employee('{self.name}', {self.pay})"
```

## `__str__`
- Readable representation — meant for **end users**
- Used by `print()` and `str()`

```python
def __str__(self):
    return f"{self.name} — Rs.{self.pay}"
```

## Arithmetic Dunders
```python
def __add__(self, other):    # emp1 + emp2
    return self.pay + other.pay

def __len__(self):           # len(emp1)
    return len(self.name)
```

## Common Dunder Methods
| Method        | Triggered by        |
|---------------|---------------------|
| `__init__`    | `ClassName()`       |
| `__str__`     | `print()`, `str()`  |
| `__repr__`    | `repr()`            |
| `__len__`     | `len()`             |
| `__add__`     | `+`                 |
| `__eq__`      | `==`                |
| `__lt__`      | `<`                 |

## Key Rule
Always define `__repr__`. Define `__str__` when you want a
different, friendlier version for users.
