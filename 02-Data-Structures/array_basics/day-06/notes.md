# Day 06 Notes

## Problem 1: Valid Palindrome (LC 125)

### Pattern
Two Pointers

### Key Idea
- Use two pointers: left and right.
- Skip non-alphanumeric characters.
- Compare characters in lowercase.
- If mismatch occurs, return False.
- If all valid characters match, return True.

### Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Problem 2: Best Time to Buy and Sell Stock (LC 121)

### Pattern
Array Traversal / Tracking Minimum

### Key Idea
- Maintain the minimum stock price seen so far.
- For every current price:
  - Calculate potential profit.
  - Update maximum profit if current profit is greater.
- Update minimum price whenever a lower price is found.

### Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## What I Learned Today

1. How to solve palindrome problems using Two Pointers.
2. How to skip unwanted characters efficiently.
3. How to compare characters without considering case sensitivity.
4. How to track minimum values while traversing an array.
5. How to calculate maximum profit in a single pass.
