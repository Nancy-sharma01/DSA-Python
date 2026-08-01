# Day 27 - Linked List Basics

## 📚 Topic Covered
- Introduction to Linked Lists
- Understanding Nodes
- `head`, `next`, and pointer references
- Traversing a Linked List
- Fast & Slow Pointer Technique
- Modifying links in a Linked List

## ✅ Problems Solved

### 1. LeetCode 876 - Middle of the Linked List
- Difficulty: Easy
- Approach:
  - Used two pointers (`slow` and `fast`).
  - `slow` moves one step at a time.
  - `fast` moves two steps at a time.
  - When `fast` reaches the end, `slow` points to the middle node.
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

### 2. LeetCode 83 - Remove Duplicates from Sorted List
- Difficulty: Easy
- Approach:
  - Traverse the linked list using `current`.
  - If two consecutive nodes have the same value:
    - Skip the duplicate node by changing the link.
  - Otherwise, move to the next node.
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

---

## 🧠 What I Learned Today

- A linked list is made up of **nodes**, where each node stores:
  - a value (`val`)
  - a reference to the next node (`next`)
- `head` is **not** a Python keyword. It is simply a variable that points to the first node.
- Linked Lists do not support indexing like arrays.
- Traversal is done by repeatedly moving to `current.next`.
- Multiple variables (like `head` and `current`) can point to the same node.
- To delete a node in a singly linked list, we update the links instead of shifting elements.
- The Fast & Slow Pointer technique is an efficient way to find the middle of a linked list.

---

## 🚀 Progress

- ✅ Learned Linked List fundamentals
- ✅ Solved first Linked List problems
- ✅ Understood pointer manipulation
- ✅ Ready to explore more Linked List problems
