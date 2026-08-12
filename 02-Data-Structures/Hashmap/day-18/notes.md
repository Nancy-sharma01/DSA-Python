# Day 18 Notes - Hash Maps (Part 2)

## 1. Frequency Counting Pattern

Used when a problem asks:
- How many times does an element appear?
- Do we have enough occurrences?
- Compare frequencies.

### Steps

1. Create an empty dictionary.
2. Count the frequency of every element.
3. Traverse the required data.
4. Decrease the count after using an element.
5. If count becomes unavailable, return False.

### Template

```python
freq = {}

for item in data:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
```

Using elements:

```python
for item in target:
    if item not in freq or freq[item] == 0:
        return False

    freq[item] -= 1

return True
```

---

## 2. One-to-One Mapping Pattern

Used when one value must always correspond to exactly one other value.

Example:

```
a → x
b → y
c → z
```

Invalid:

```
a → x
b → x
```

or

```
a → x
a → y
```

---

### Two Dictionary Technique

```
mapST
Source → Target

mapTS
Target → Source
```

This ensures consistency in both directions.

---

### Template

```python
mapST = {}
mapTS = {}

for s_char, t_char in zip(s, t):

    if s_char in mapST and mapST[s_char] != t_char:
        return False

    if t_char in mapTS and mapTS[t_char] != s_char:
        return False

    mapST[s_char] = t_char
    mapTS[t_char] = s_char

return True
```

---

## Python Functions Used

### zip()

Iterates through two sequences simultaneously.

Example:

```python
s = "abc"
t = "xyz"

for a, b in zip(s, t):
    print(a, b)
```

Output

```
a x
b y
c z
```

---

## HashMap Patterns Learned So Far

### Frequency Counting
Stores:

```
element → count
```

Examples:
- Ransom Note
- Valid Anagram
- Majority Element

---

### Character Mapping
Stores:

```
element → element
```

Examples:
- Isomorphic Strings
- Word Pattern
- Custom Mapping Problems

---

## Interview Takeaway

Whenever you see a problem involving:

- Counting occurrences → Think Frequency HashMap.
- Maintaining relationships → Think Mapping HashMap.
- One-to-one correspondence → Use Two HashMaps.

Choosing the correct HashMap pattern is the key to solving these problems efficiently.
