# Topic 01 — Classes & Instances

## What is a Class?
- A **blueprint** for creating objects
- Groups data (attributes) and functions (methods) together
- Think of it like a template — one class, many objects

## What is an Instance?
- The actual object created from a class
- `emp1`, `emp2` are both instances of the `Employee` class
- Each instance holds its own data

## The `__init__` Method
- Called the **constructor**
- Runs **automatically** when an object is created
- Used to set the initial attributes of the object

## The `self` Keyword
- Refers to **the instance itself**
- Python passes it automatically — you don't pass it manually
- `self.name` → accesses the `name` attribute of that specific object

## Two Ways to Call a Method
```python
emp1.fullname()           # from the instance — normal way
Employee.fullname(emp1)   # from the class — pass instance manually
```

## Naming Conventions
- Class names → `PascalCase` — `Employee`, `StudentTracker`
- Methods and variables → `snake_case` — `full_name`, `apply_raise`
- `self` is just a convention, not a keyword — but always use it
