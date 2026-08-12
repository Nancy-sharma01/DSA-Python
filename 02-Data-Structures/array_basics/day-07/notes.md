# Day 07 Notes

## Concepts Learned

### 1. 2D Arrays

A 2D array is an array of arrays.

Example:

accounts = [
[1, 2, 3],
[3, 2, 1]
]

To traverse a 2D array:

for row in accounts:
print(row)

### 2. sum() Function

The sum() function returns the sum of all elements in a list.

Example:

nums = [1, 2, 3]
total = sum(nums)

Output: 6

### 3. Two Pointer Technique

Two pointers are used to process arrays efficiently while maintaining O(1) extra space.

In LeetCode 80, a pointer k tracks the position where the next valid element should be placed.

### 4. In-place Array Modification

Instead of creating a new array, modify the existing array directly.

Benefits:

* Saves memory
* Often required in coding interviews
* Improves efficiency

## Problems Practiced

1. LeetCode 1672 - Richest Customer Wealth
2. LeetCode 80 - Remove Duplicates from Sorted Array II

## Key Takeaway

Understanding array traversal and two-pointer techniques is essential because many interview questions build upon these concepts.
