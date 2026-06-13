# Topic 03 — Class Methods & Static Methods

## Regular Methods
- Automatically receive the **instance** (`self`) as the first argument
- Used for operations that need access to instance data

## Class Methods
- Use the `@classmethod` decorator
- Automatically receive the **class** (`cls`) as the first argument
- Most common use: **alternative constructors** — different ways to create objects

```python
@classmethod
def from_string(cls, emp_str):
    name, pay = emp_str.split('-')
    return cls(name, int(pay))

emp = Employee.from_string("Kamal-50000")
```

## Static Methods
- Use the `@staticmethod` decorator
- Receive **neither** the instance nor the class automatically
- Behave like regular functions — included in the class because they're logically related

```python
@staticmethod
def is_workday(day):
    return day.weekday() < 5   # 0=Mon, 6=Sun
```

## How to Decide Which to Use
| Need access to...     | Use            |
|-----------------------|----------------|
| Instance data (self)  | Regular method |
| Class data (cls)      | Class method   |
| Neither               | Static method  |

## Key Point
If you find yourself not using `self` or `cls` inside a method,
it should probably be a static method.
