# Day 17 Notes - Hash Maps

## What is a Hash Map?

A Hash Map is a data structure that stores information in **key-value pairs**.

Example:

```python
student = {
    "name": "Nancy",
    "age": 21
}
```

Python implements Hash Maps using the `dict` data type.

---

# Why Hash Maps?

Without a Hash Map:

Searching an element in an array takes **O(n)**.

With a Hash Map:

Searching a key takes **O(1)** average time.

---

# Basic Dictionary Operations

## Create

```python
d = {}
```

---

## Insert

```python
d["apple"] = 10
```

---

## Access

```python
print(d["apple"])
```

---

## Update

```python
d["apple"] = 20
```

---

## Delete

```python
del d["apple"]
```

---

## Check Key

```python
if "apple" in d:
    print("Found")
```

---

## Dictionary Methods

```python
d.keys()
d.values()
d.items()
d.get(key)
```

---

# Frequency Counting Pattern

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

Explanation:

* If the key exists, increase its count.
* Otherwise, start the count from `0` and then add `1`.

---

# Hash Map vs Set

## Hash Map (`dict`)

Stores:

```
Key → Value
```

Example:

```python
{
"Alice": 95,
"Bob": 88
}
```

---

## Set

Stores only unique values.

Example:

```python
{
95,
88
}
```

---

# Two Sum (Brute Force)

Idea:

Check every possible pair using nested loops.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

Time Complexity:

```
O(n²)
```

---

# Two Sum (Optimal - Hash Map)

Algorithm:

1. Create an empty dictionary.
2. Traverse the array.
3. Compute:

```python
complement = target - nums[i]
```

4. If the complement already exists in the dictionary:

```python
return [seen[complement], i]
```

5. Otherwise:

```python
seen[nums[i]] = i
```

---

## Optimal Code

```python
seen = {}

for i in range(len(nums)):
    complement = target - nums[i]

    if complement in seen:
        return [seen[complement], i]

    seen[nums[i]] = i
```

---

# Complexity

## Brute Force

* Time: **O(n²)**
* Space: **O(1)**

## Hash Map

* Time: **O(n)**
* Space: **O(n)**

---

# Common Interview Patterns

Use a Hash Map when the problem involves:

* Frequency counting
* Fast lookup
* Duplicates
* Pair sum
* Character counting
* Mapping one value to another
* Previously seen elements

---

# Key Takeaways

* Hash Maps reduce repeated searching.
* Dictionary lookup is **O(1)** on average.
* `dict.get()` is useful for counting frequencies.
* Store **value → index** for lookup problems.
* The complement technique is the core idea behind Two Sum.
* Think: **"Can I store previous information to avoid searching again?"**

---

**Day 17 Complete ✅**
