# Day 02 - Time Complexity & Object-Oriented Programming (OOP)

## What is Time Complexity?

Time Complexity measures how the execution time of an algorithm grows as the input size increases.

It helps us compare different solutions and choose the most efficient one.

---

## Common Time Complexities

| Complexity | Name         | Example                    |
| ---------- | ------------ | -------------------------- |
| O(1)       | Constant     | Accessing an array element |
| O(log n)   | Logarithmic  | Binary Search              |
| O(n)       | Linear       | Traversing an array        |
| O(n log n) | Linearithmic | Merge Sort                 |
| O(n²)      | Quadratic    | Nested Loops               |

---

## O(1) - Constant Time

The number of operations remains the same regardless of input size.

```python
arr = [10, 20, 30, 40]

print(arr[0])
```

**Time Complexity:** O(1)

---

## O(n) - Linear Time

Execution time increases linearly with input size.

```python
arr = [1, 2, 3, 4, 5]

for num in arr:
    print(num)
```

**Time Complexity:** O(n)

---

## O(n²) - Quadratic Time

Occurs when nested loops are used.

```python
arr = [1, 2, 3]

for i in arr:
    for j in arr:
        print(i, j)
```

**Time Complexity:** O(n²)

---

## Space Complexity

Space Complexity refers to the amount of memory used by an algorithm.

```python
numbers = [1, 2, 3, 4, 5]
```

Since extra memory is used to store elements, the space complexity is:

**Space Complexity:** O(n)

---

# Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming paradigm that organizes code using classes and objects.

It improves code reusability, maintainability, and scalability.

---

## Class

A class is a blueprint for creating objects.

```python
class Student:
    pass
```

---

## Object

An object is an instance of a class.

```python
s1 = Student()
```

---

## Constructor

A constructor is automatically called when an object is created.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## Instance Variable

Variables that belong to an object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Here, `name` is an instance variable.

---

## Method

Functions defined inside a class are called methods.

```python
class Student:

    def greet(self):
        print("Hello")
```

---

## Encapsulation

Encapsulation means binding data and methods together inside a class.

```python
class Student:

    def __init__(self):
        self.name = "Nancy"
```

---

## Inheritance

Inheritance allows one class to acquire properties and methods of another class.

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):
    pass
```

`Dog` inherits from `Animal`.

---

## Polymorphism

The same method name can behave differently in different classes.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

---

## Abstraction

Abstraction hides implementation details and shows only essential functionality.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

# Key Takeaways

* Time Complexity helps analyze algorithm efficiency.
* O(1), O(n), and O(n²) are the most common complexities in beginner DSA.
* OOP helps organize code using classes and objects.
* Four major pillars of OOP:

  * Encapsulation
  * Inheritance
  * Polymorphism
  * Abstraction

---

**Day 02 Completed ✅**

Topics Revised:

* Time Complexity
* Space Complexity
* Classes & Objects
* Constructors
* Methods
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
