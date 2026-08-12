# Day 22 - Hash Set & Consecutive Sequences

## 📚 Topic

* Hash Set
* Hash Map Revision
* Consecutive Sequence Pattern

## ✅ Problems Solved

### 1. LeetCode 219 - Contains Duplicate II (Easy)

**Concepts:**

* Hash Map
* Storing the last seen index
* Distance between duplicate elements

**Approach:**

* Store the latest index of each element in a dictionary.
* If the element appears again and the index difference is less than or equal to `k`, return `True`.
* Otherwise, update its latest index.

**Complexity:**

* Time: **O(n)**
* Space: **O(n)**

---

### 2. LeetCode 128 - Longest Consecutive Sequence (Medium)

**Concepts:**

* Hash Set
* Sequence Detection
* Optimized O(n) Traversal

**Approach:**

* Convert the array into a set for O(1) lookups.
* Only start counting when the current number has no predecessor (`num - 1` is not in the set).
* Expand the sequence forward while the next consecutive number exists.
* Track the maximum sequence length found.

**Complexity:**

* Time: **O(n)**
* Space: **O(n)**

---

## 🧠 What I Learned

* Difference between using a Hash Map and a Hash Set.
* A set is useful when only existence checks are required.
* In consecutive sequence problems, only start counting from the beginning of a sequence.
* Checking `num - 1` prevents counting the same sequence multiple times.
* Since the first element is already counted, the loop should check `pt + 1` instead of `pt`.
* Maintain a separate `longest` variable because each sequence has its own `count`, and we need to remember the maximum across all sequences.

---

## 🚀 Progress

* **Day:** 22 / 70
* **Problems Solved Today:** 2
* **Difficulty:** Easy + Medium

Consistency > Perfection. One step closer to becoming interview-ready!
