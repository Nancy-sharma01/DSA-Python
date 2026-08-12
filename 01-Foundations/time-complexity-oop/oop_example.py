# ============================================================
# Day 02 - Object-Oriented Programming (OOP) in Python
# Concepts: Class/Object, Encapsulation, Inheritance,
#           Polymorphism, Abstraction
# ============================================================

from abc import ABC, abstractmethod


# ── 1. Class and Object ──────────────────────────────────────

class Student:
    """Represents a student with name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Prints a greeting message."""
        print(f"Hi, I am {self.name} and I am {self.age} years old.")


student = Student("Nancy", 21)
student.introduce()
# Output: Hi, I am Nancy and I am 21 years old.


# ── 2. Encapsulation ─────────────────────────────────────────

class BankAccount:
    """Demonstrates encapsulation using private variables."""

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private variable

    def deposit(self, amount):
        """Adds amount to balance."""
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def get_balance(self):
        """Returns current balance."""
        return self.__balance


account = BankAccount("Nancy", 1000)
account.deposit(500)
# Output: Deposited 500. New balance: 1500
print("Balance:", account.get_balance())
# Output: Balance: 1500
# print(account.__balance)  # Would raise AttributeError — private!


# ── 3. Inheritance ───────────────────────────────────────────

class Animal:
    """Base class for all animals."""

    def __init__(self, name):
        self.name = name

    def sound(self):
        """Returns the sound the animal makes."""
        print(f"{self.name} makes a sound")


class Dog(Animal):
    """Dog inherits from Animal."""

    def sound(self):
        print(f"{self.name} barks")


class Cat(Animal):
    """Cat inherits from Animal."""

    def sound(self):
        print(f"{self.name} meows")


dog = Dog("Bruno")
dog.sound()
# Output: Bruno barks

cat = Cat("Whiskers")
cat.sound()
# Output: Whiskers meows


# ── 4. Polymorphism ──────────────────────────────────────────
# Same method name, different behavior based on object type

animals = [Dog("Bruno"), Cat("Whiskers"), Animal("Generic")]
for animal in animals:
    animal.sound()
# Output:
# Bruno barks
# Whiskers meows
# Generic makes a sound


# ── 5. Abstraction ───────────────────────────────────────────

class Vehicle(ABC):
    """Abstract base class — cannot be instantiated directly."""

    @abstractmethod
    def start(self):
        """Every vehicle must implement start()."""
        pass

    @abstractmethod
    def stop(self):
        """Every vehicle must implement stop()."""
        pass


class Car(Vehicle):
    """Concrete class implementing Vehicle."""

    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")


class Bike(Vehicle):
    """Concrete class implementing Vehicle."""

    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


car = Car()
car.start()   # Output: Car engine started
car.stop()    # Output: Car engine stopped

bike = Bike()
bike.start()  # Output: Bike started
bike.stop()   # Output: Bike stopped

# vehicle = Vehicle()  # Would raise TypeError — abstract class!
