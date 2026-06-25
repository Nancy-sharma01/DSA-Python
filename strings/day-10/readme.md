# Day-10: Strings Basics 🚀

## Topics Covered

Today I started learning **Strings in Python** as a part of my DSA Challenge.

Topics covered:

- What is a String?
- String Indexing
- String Traversal
- String Slicing
- String Concatenation
- String Repetition
- Common String Methods
- Searching in Strings
- Count and Find Operations

---

## What is a String?

A string is a sequence of characters.

Example:

```python
s = "Nancy"
```

Characters are stored using indexes:

```
N   a   n   c   y
0   1   2   3   4
```

---

## String Indexing

Accessing characters using index.

```python
s = "Nancy"

print(s[0])
print(s[-1])
```

Output:

```
N
y
```

---

## Traversing a String

Using for loop:

```python
s = "Python"

for ch in s:
    print(ch)
```

Using index:

```python
for i in range(len(s)):
    print(s[i])
```

---

## String Slicing

Syntax:

```python
string[start:end]
```

Example:

```python
s = "Python"

print(s[0:3])
print(s[2:])
print(s[::-1])
```

Output:

```
Pyt
thon
nohtyP
```

---

## String Concatenation

Joining two strings.

```python
first = "Nancy"
last = "Sharma"

print(first + " " + last)
```

Output:

```
Nancy Sharma
```

---

## String Repetition

Using * operator.

```python
print("Hi " * 3)
```

Output:

```
Hi Hi Hi
```

---

## Common String Methods

```python
s = "hello world"

print(len(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
```

---

## Checking Characters

```python
s = "abc123"

print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
```

---

## Searching in String

Using `in` keyword:

```python
s = "hello"

print("e" in s)
print("z" in s)
```

Output:

```
True
False
```

---

## Count and Find

### count()

Counts occurrences of a character.

```python
s = "banana"

print(s.count("a"))
```

Output:

```
3
```

### find()

Returns first index of character.

```python
s = "banana"

print(s.find("n"))
```

Output:

```
2
```

---

## Time Complexity

| Operation | Complexity |
|---|---|
| Access character | O(1) |
| Traversal | O(n) |
| Search | O(n) |
| Slicing | O(k) |

---

## Practice

Today I focused on understanding the basics of Strings.

Next step:

- Practice string problems
- Apply:
  - Traversal
  - Reversing
  - Comparison
  - Counting
  - Two Pointer Technique

---

## Key Takeaways

- Strings are immutable in Python.
- Indexing helps access characters.
- Slicing helps extract parts of strings.
- Most string problems involve:
  - Traversal
  - Comparison
  - Counting
  - Reversing

---

## Day-10 Completed ✅
