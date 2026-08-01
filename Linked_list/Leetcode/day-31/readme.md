# Day 31 - Merge Two Sorted Lists

## 🧩 Problem
**LeetCode 21 - Merge Two Sorted Lists**

### 🔗 Problem Link
https://leetcode.com/problems/merge-two-sorted-lists/

---

## 🎯 Objective
Merge two sorted linked lists into a single sorted linked list by rearranging the existing nodes without creating new data nodes.

---

## 💡 Approach
- Created a **dummy node** to simplify handling the head of the merged list.
- Used a **tail pointer** to build the merged list.
- Compared the current nodes of both linked lists.
- Attached the smaller node to the merged list and moved the corresponding pointer.
- After one list became empty, directly attached the remaining nodes of the other list.

---

## 🧠 Concepts Learned
- Linked List Traversal
- Pointer Manipulation
- Dummy Node Technique
- Tail Pointer
- Merging Two Sorted Linked Lists
- Time & Space Complexity

---

## ⏱️ Complexity
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(1)`

Where:
- `n` = length of first linked list
- `m` = length of second linked list

---

## 📚 Key Takeaways
- The **dummy node** simplifies edge cases when building a linked list.
- The **tail pointer** always points to the last node of the merged list.
- Once one list is exhausted, the remaining nodes of the other list can be attached directly.
- Proper pointer movement is essential to avoid infinite loops.

---

## 🚀 Status
✅ Solved successfully as part of my **#70DaysOfDSA Challenge**

**Day:** 31/70