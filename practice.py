# ================================
# Topic 01: Classes & Instances
# ================================
# After watching Corey Schafer OOP Part 1,
# rewrite these from memory. Don't copy.

# ----- EXERCISE 1: Basic class -----
# Student class with name, grade, age

class Student:
    def __init__(self, name, grade, age):
        self.name  = name
        self.grade = grade
        self.age   = age

    def info(self):
        return f"{self.name} (Grade {self.grade}, Age {self.age})"

    def is_senior(self):
        # Senior if Grade 11 or above
        return self.grade >= 11


# ----- TEST -----
s1 = Student("Kamal", 10, 15)
s2 = Student("Nimal", 12, 17)

print(s1.info())        # Kamal (Grade 10, Age 15)
print(s2.info())        # Nimal (Grade 12, Age 17)
print(s1.is_senior())   # False
print(s2.is_senior())   # True


# ----- EXERCISE 2: Write your own -----
# Book class — title, author, pages
# method: summary() → "Title by Author — N pages"

class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def summary(self):
        return f"{self.title} by {self.author} — {self.pages} pages"


b1 = Book("Clean Code", "Robert Martin", 431)
print(b1.summary())


# ----- CHALLENGE (write this yourself) -----
# Vehicle class — brand, model, year
# method: age()         → current year - self.year
# method: description() → "2019 Toyota Corolla"
# TODO: Write it yourself — no copying!

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = int(year)
    
    def age(self):
        current_year = 2026
        return (current_year - self.year)
    
    def description(self):
        return f"{self.year} {self.brand} {self.model}"
    
#test
car1 = Vehicle("TOYOTA", "Corolla", 2019)

print(car1.age())
print(car1.description())
