# Python Revision Notes

## Variables and Data Types

Python supports multiple built-in data types:

* `int`
* `float`
* `str`
* `bool`
* `list`
* `tuple`
* `dict`
* `set`

### Example

```python
name = "Nancy"
age = 21
cgpa = 7.38
```

---

## Input and Output

```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

## Conditional Statements

```python
age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## Loops

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Functions

```python
def square(num):
    return num * num

print(square(5))
```

---

## Lists

Lists are ordered and mutable collections.

```python
fruits = ["apple", "banana", "mango"]

fruits.append("orange")
fruits.remove("banana")

print(fruits)
```

---

## Tuples

Tuples are ordered and immutable collections.

```python
coordinates = (10, 20)

print(coordinates[0])
```

---

## Dictionaries

Dictionaries store data as key-value pairs.

```python
student = {
    "name": "Nancy",
    "branch": "CSE"
}

print(student["name"])
```

---

## Sets

Sets store unique values.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

---

## List Comprehensions

A concise way to create lists.

```python
squares = [x * x for x in range(5)]

print(squares)
```

---

## File Handling

### Reading a File

```python
with open("file.txt", "r") as file:
    data = file.read()

print(data)
```

### Writing to a File

```python
with open("file.txt", "w") as file:
    file.write("Hello World")
```

---

## Exception Handling

```python
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")
```

---

## Key Takeaways

* Python syntax is simple and readable.
* Lists, dictionaries, and sets are heavily used in DSA.
* Functions help create reusable code.
* Exception handling prevents program crashes.
* Strong Python fundamentals make DSA implementation easier.
