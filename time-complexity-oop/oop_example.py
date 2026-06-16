# Day 02 - OOP Examples in Python

from abc import ABC, abstractmethod

# -------------------------

# Class and Object

# -------------------------

class Student:

```
def __init__(self, name, age):
    self.name = name
    self.age = age

def introduce(self):
    print(f"Hi, I am {self.name} and I am {self.age} years old.")
```

# -------------------------

# Inheritance & Polymorphism

# -------------------------

class Animal:

```
def sound(self):
    print("Animal makes a sound")
```

class Dog(Animal):

```
def sound(self):
    print("Dog barks")
```

class Cat(Animal):

```
def sound(self):
    print("Cat meows")
```

# -------------------------

# Abstraction

# -------------------------

class Vehicle(ABC):

```
@abstractmethod
def start(self):
    pass
```

class Car(Vehicle):

```
def start(self):
    print("Car Started")
```

# -------------------------

# Creating Objects

# -------------------------

student = Student("Nancy", 21)
student.introduce()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

car = Car()
car.start()
