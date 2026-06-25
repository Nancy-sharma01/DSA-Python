# Day-10 Notes: Strings 🚀

## What is a String?

A string is a sequence of characters.

Example:

```python
s = "Python"
```

Indexes:

```
P  y  t  h  o  n
0  1  2  3  4  5
```

---

## String Indexing

Access characters using index.

```python
s = "Python"

print(s[0])    # P
print(s[-1])   # n
```

Negative indexing starts from the end.

```
P  y  t  h  o  n
0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

---

## Traversing String

Using for loop:

```python
s = "hello"

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
# Pyt

print(s[2:])
# thon

print(s[::-1])
# nohtyP
```

---

## Concatenation

Joining strings using `+`.

```python
a = "Hello"
b = "World"

print(a + " " + b)
```

Output:

```
Hello World
```

---

## Repetition

Using `*`

```python
print("Hi " * 3)
```

Output:

```
Hi Hi Hi
```

---

## Important String Methods

### len()

Returns length of string.

```python
s = "Python"

print(len(s))
```

Output:

```
6
```

---

### upper()

Converts string to uppercase.

```python
s = "hello"

print(s.upper())
```

Output:

```
HELLO
```

---

### lower()

Converts string to lowercase.

```python
s = "HELLO"

print(s.lower())
```

---

### capitalize()

Makes first character uppercase.

```python
s = "python"

print(s.capitalize())
```

Output:

```
Python
```

---

### title()

Makes first letter of every word uppercase.

```python
s = "hello world"

print(s.title())
```

Output:

```
Hello World
```

---

## Checking Characters

### isalpha()

Checks only alphabets.

```python
"abc".isalpha()
```

True

---

### isdigit()

Checks only digits.

```python
"123".isdigit()
```

True

---

### isalnum()

Checks alphabets + numbers.

```python
"abc123".isalnum()
```

True

---

## Searching in String

Using `in`:

```python
s = "hello"

print("e" in s)
```

Output:

```
True
```

---

## count()

Counts occurrences.

```python
s = "banana"

print(s.count("a"))
```

Output:

```
3
```

---

## find()

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

## Important Points

- Strings are immutable in Python.
- We cannot change a character directly.

Example:

```python
s = "hello"

s[0] = "H"
```

This gives error.

---

## String Problem Approach

Whenever solving string problems:

1. Traverse the string
2. Compare characters
3. Count frequency
4. Reverse if needed
5. Use two pointers when required

---

## Time Complexity

| Operation | Complexity |
|---|---|
| Access | O(1) |
| Traversal | O(n) |
| Search | O(n) |
| Slicing | O(k) |

---

Day-10 Completed ✅
