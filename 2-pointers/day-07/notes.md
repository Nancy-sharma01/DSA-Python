# Day 07 - Two Pointers Technique

## Definition

Two Pointers is an optimization technique in which two indices (pointers) are used to traverse an array or string efficiently. It is commonly used to reduce the time complexity of problems from **O(n²)** to **O(n)**.

---

## Why Use Two Pointers?

Many problems can be solved using nested loops, but that results in **O(n²)** time complexity.

### Brute Force

```python
for i in range(n):
    for j in range(i + 1, n):
        if condition:
            return answer
```

Time Complexity: **O(n²)**

### Two Pointers

```python
left = 0
right = len(arr) - 1

while left < right:
    # process elements
```

Time Complexity: **O(n)**

---

## Types of Two Pointers

### 1. Opposite Direction Pointers

Pointers start from opposite ends and move toward each other.

```text
1  2  3  4  5
L           R
```

#### Applications

* Valid Palindrome
* Two Sum II
* Container With Most Water
* 3Sum

#### Template

```python
left = 0
right = len(arr) - 1

while left < right:

    if condition_1:
        left += 1

    elif condition_2:
        right -= 1

    else:
        return answer
```

---

### 2. Same Direction Pointers

Both pointers move in the same direction.

```text
0 1 2 3 4 5
L
R
```

One pointer reads elements while the other tracks the position for updates.

#### Applications

* Remove Duplicates from Sorted Array
* Remove Element
* Move Zeroes

---

## Example 1: Valid Palindrome

String:

```text
m a d a m
L       R
```

Compare characters at both ends.

If they match:

```python
left += 1
right -= 1
```

Continue until the pointers meet.

### Code

```python
def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

---

## Example 2: Two Sum II

Array:

```text
2  3  4  7  11
L            R
```

Target = 9

### Logic

If current sum > target:

```python
right -= 1
```

If current sum < target:

```python
left += 1
```

If current sum == target:

```python
return answer
```

---

## Advantages

* Reduces time complexity from O(n²) to O(n)
* Uses constant extra space O(1)
* Easy to implement
* Frequently asked in coding interviews

---

## How to Identify Two Pointer Problems?

Look for these clues:

* Sorted arrays
* Pair finding problems
* Triplet finding problems
* Palindrome checking
* Comparing elements from both ends
* Need for O(n) optimization

---

## Complexity Analysis

| Approach     | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Brute Force  | O(n²)           | O(1)             |
| Two Pointers | O(n)            | O(1)             |

---

## Problems Practiced

1. LeetCode 125 - Valid Palindrome
2. LeetCode 167 - Two Sum II
3. LeetCode 11 - Container With Most Water
4. LeetCode 15 - 3Sum

---

## Key Takeaways

* Two Pointers is a problem-solving technique, not a data structure.
* It is mainly used for arrays and strings.
* The technique significantly improves efficiency by avoiding unnecessary comparisons.
* Common patterns include opposite-direction and same-direction pointers.
* Always consider Two Pointers when dealing with sorted arrays, palindromes, or pair-finding problems.
