# Day 16 Notes 📝

## 1. Frequency Map

A frequency map stores how many times each element appears.

Example:

```python
s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Output

```python
{
    'b': 1,
    'a': 3,
    'n': 2
}
```

---

## 2. Understanding `.get()`

Syntax

```python
dictionary.get(key, default_value)
```

Example

```python
freq.get('a', 0)
```

- Returns the value of `'a'` if it exists.
- Otherwise returns `0`.

Equivalent code:

```python
if ch in freq:
    freq[ch] += 1
else:
    freq[ch] = 1
```

---

## 3. Frequency Map Pattern

```python
freq = {}

for item in collection:
    freq[item] = freq.get(item, 0) + 1
```

This pattern appears in many interview questions.

---

## 4. Generating All Substrings

```python
for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j+1]
```

Time Complexity

```
O(n²) substrings
```

---

## 5. Why Normal Sliding Window Doesn't Work

Sliding Window works well when:

- The window can become valid by simply moving the left pointer.

Example:

- Longest Substring Without Repeating Characters
- Maximum Average Subarray
- Fruit Into Baskets

LeetCode 395 is different.

Condition:

> Every character inside the substring must appear at least `k` times.

Removing characters only from the left cannot always fix the window.

Hence, the standard Sliding Window template is insufficient.

---

## 6. Divide & Conquer Idea

Steps:

1. Count frequency of every character.
2. Find any character whose frequency is less than `k`.
3. That character can never be part of a valid answer.
4. Split the string around that character.
5. Recursively solve each part.
6. Return the maximum answer.

Pseudo Code

```
count frequencies

for every character
    if frequency < k
        split string
        solve left part
        solve right part
        return maximum

return length of string
```

---

## 7. Important Learning

Today was less about solving one problem and more about understanding a new pattern.

Learned:

- Frequency Maps
- Python Dictionary
- `.get()` Method
- Substring Generation
- Divide & Conquer
- Why choosing the correct algorithm matters more than forcing a familiar one.

---

## Interview Tips

Always ask yourself:

- Is this a frequency problem?
- Can a hash map help?
- Does Sliding Window satisfy the problem constraints?
- Is there another paradigm (Greedy, Divide & Conquer, Binary Search, etc.) that fits better?

Pattern recognition is one of the most valuable DSA skills.
