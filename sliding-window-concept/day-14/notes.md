# Day 14 - Sliding Window (Fixed Size)

## What is Sliding Window?

Sliding Window is an optimization technique used to solve problems involving **subarrays** or **substrings** efficiently.

Instead of recalculating the result for every window, we update it by:
- Adding the new element entering the window.
- Removing the element leaving the window.

This reduces the time complexity from **O(n × k)** to **O(n)**.

---

## When to Use Sliding Window?

Look for these keywords:

- Subarray
- Substring
- Continuous
- Consecutive
- Maximum / Minimum
- Longest / Shortest

---

## Types of Sliding Window

### 1. Fixed Size Sliding Window
- Window size remains constant.
- Example: Find the maximum average of a subarray of size `k`.

### 2. Variable Size Sliding Window
- Window size changes depending on the condition.
- Example: Longest substring without repeating characters.

---

## Algorithm (Fixed Size)

1. Calculate the sum of the first `k` elements.
2. Store it as the maximum sum.
3. Move the window one element at a time.
4. Add the new element entering the window.
5. Remove the element leaving the window.
6. Update the maximum sum.
7. Return the maximum average.

---

## Key Formula

```python
current_sum += nums[i] - nums[i - k]
```

- `nums[i]` → New element entering the window.
- `nums[i - k]` → Old element leaving the window.

---

## Time Complexity

- Initial window sum: O(k)
- Sliding the window: O(n - k)

Overall: **O(n)**

---

## Space Complexity

**O(1)**

---

## Problem Solved

- LeetCode 643 - Maximum Average Subarray I

---

## What I Learned

- Introduction to the Sliding Window technique.
- Fixed-size window optimization.
- Updating the window without recalculating the sum.
- Difference between Python 2 and Python 3 division.
