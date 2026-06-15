
---

### 3️⃣ `Python_Foundation/basics_revision.py`

```python
# Variables and Data Types
name = "Nancy"
age = 21
cgpa = 7.38

print(name, age, cgpa)

# Conditional Statements
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Loops
for i in range(5):
    print(i)

# Functions
def square(num):
    return num * num

print(square(5))

# Lists
numbers = [1, 2, 3, 4]
numbers.append(5)

# Dictionaries
student = {
    "name": "Nancy",
    "branch": "CSE"
}

print(student["name"])

# List Comprehension
squares = [x * x for x in range(5)]
print(squares)
