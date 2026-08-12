# Day 09 - Arrays Revision & Patterns

## What I Learned

Arrays are the foundation of Data Structures. Most array problems are solved using a few common patterns rather than memorizing solutions.

---

## 1. Traversal

Visit every element once.

```python
arr = [10, 20, 30, 40]

for num in arr:
    print(num)
```

Time Complexity: **O(n)**

Used in:

* Searching
* Counting
* Finding max/min

---

## 2. Running Maximum

Keep track of the largest element seen so far.

```python
arr = [4, 2, 8, 1]

max_ele = arr[0]

for num in arr:
    if num > max_ele:
        max_ele = num

print(max_ele)
```

Time Complexity: **O(n)**

Used in:

* Largest Element
* Stock Profit Problems

---

## 3. Counting Pattern

Count occurrences of an element.

```python
arr = [1, 2, 2, 3, 2]

count = 0

for num in arr:
    if num == 2:
        count += 1

print(count)
```

Time Complexity: **O(n)**

---

## 4. Two Pointers

Use two indices to reduce nested loops.

```python
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
```

Time Complexity: **O(n)**

Used in:

* Reverse Array
* Palindrome Problems
* Sorted Array Questions

---

## 5. Sliding Window (Introduction)

Efficiently process subarrays.

```python
arr = [1, 2, 3, 4, 5]
k = 3

window_sum = sum(arr[:k])

for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i-k]

print(window_sum)
```

Used in:

* Maximum Sum Subarray
* Fixed Window Problems

---

## Common Mistakes

### Index Out Of Range

Wrong:

```python
for i in range(len(arr)+1):
```

Correct:

```python
for i in range(len(arr)):
```

### Edge Cases

Always think about:

```python
[]
[1]
All same elements
Negative numbers
```

---

## Array Patterns Checklist

* [x] Traversal
* [x] Linear Search
* [x] Largest Element
* [x] Counting
* [x] Two Pointers
* [x] Reverse Array
* [x] Palindrome
* [x] Best Time To Buy And Sell Stock
* [x] Sliding Window Basics

---

## Key Takeaways

1. Arrays are the most important beginner DSA topic.
2. Most problems use patterns, not new concepts.
3. Two Pointers and Sliding Window are interview favorites.
4. Strong array fundamentals make Strings, Hashing, and Advanced DSA easier.

## Progress

Day 01 ✅

Day 02 ✅

Day 03 ✅

Day 04 ✅

Day 05 ✅

Day 06 ✅

Day 07 ✅

Day 08 ✅

Day 09 ✅ Arrays Completed

Next Topic → Strings 🚀
