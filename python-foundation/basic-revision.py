# ============================================================
# Python Foundation - Basic Revision
# Day 1 of 70-Day DSA Challenge
# Topics: Variables, I/O, Conditionals, Loops, Functions,
#         Lists, Dictionaries, Tuples, Sets, List Comprehension
# ============================================================


# ── 1. Variables and Data Types ──────────────────────────────
name = "Nancy"
age = 21
cgpa = 7.38
is_student = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Is Student:", is_student)
# Output: Name: Nancy | Age: 21 | CGPA: 7.38 | Is Student: True


# ── 2. Input and Output ──────────────────────────────────────
# Uncomment to run interactively:
# user_name = input("Enter your name: ")
# print("Hello,", user_name)


# ── 3. Conditional Statements ────────────────────────────────
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
# Output: Eligible to vote


# ── 4. Loops ─────────────────────────────────────────────────
# For loop
print("For loop:")
for i in range(5):
    print(i, end=" ")
print()
# Output: 0 1 2 3 4

# While loop
print("While loop:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()
# Output: 1 2 3 4 5


# ── 5. Functions ─────────────────────────────────────────────
def square(num):
    """Returns the square of a number."""
    return num * num

def greet(person_name):
    """Returns a greeting message."""
    return f"Hello, {person_name}!"

print(square(5))       # Output: 25
print(greet("Nancy"))  # Output: Hello, Nancy!


# ── 6. Lists ─────────────────────────────────────────────────
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.remove("banana")
print("Fruits:", fruits)
# Output: Fruits: ['apple', 'mango', 'orange']

# Common list operations
numbers = [4, 2, 7, 1, 9]
print("Sorted:", sorted(numbers))   # Output: [1, 2, 4, 7, 9]
print("Max:", max(numbers))         # Output: 9
print("Length:", len(numbers))      # Output: 5


# ── 7. Tuples ────────────────────────────────────────────────
coordinates = (10, 20)
print("X:", coordinates[0])  # Output: X: 10
print("Y:", coordinates[1])  # Output: Y: 20
# Tuples are immutable — elements cannot be changed after creation


# ── 8. Dictionaries ──────────────────────────────────────────
student = {
    "name": "Nancy",
    "branch": "CSE",
    "cgpa": 7.38
}
print("Student Name:", student["name"])    # Output: Student Name: Nancy
print("Branch:", student.get("branch"))   # Output: Branch: CSE

# Adding a new key
student["year"] = 3
print("Updated dict:", student)


# ── 9. Sets ──────────────────────────────────────────────────
unique_numbers = {1, 2, 3, 2, 1}   # duplicates auto-removed
unique_numbers.add(4)
print("Set:", unique_numbers)       # Output: {1, 2, 3, 4}


# ── 10. List Comprehension ───────────────────────────────────
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)          # Output: [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)              # Output: [0, 2, 4, 6, 8]


# ── 11. Exception Handling ───────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
# Output: Error: Cannot divide by zero


# ── 12. File Handling (concept demo) ─────────────────────────
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello from Nancy!\n")

# Reading from a file
with open("sample.txt", "r") as file:
    data = file.read()
    print("File content:", data)
# Output: File content: Hello from Nancy!
