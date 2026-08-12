# Day 17 - Hash Maps (Dictionary in Python)

## 🎯 Goal

Understand the fundamentals of **Hash Maps (Dictionaries in Python)** and learn how they optimize problems from **O(n²)** to **O(n)**.

---

## 📚 Topics Covered

* Introduction to Hash Maps
* Dictionary (`dict`) in Python
* Creating and updating dictionaries
* Accessing, deleting, and searching keys
* Dictionary methods (`get()`, `keys()`, `values()`, `items()`)
* Frequency counting using Hash Maps
* Hash Map vs Set
* Time Complexity of Hash Maps
* Hash Map interview patterns

---

## 🧠 Problem Solved

### LeetCode 1 - Two Sum

* **Difficulty:** Easy

* **Approach 1:** Brute Force (Nested Loops)

  * Time Complexity: **O(n²)**
  * Space Complexity: **O(1)**

* **Approach 2:** Hash Map (Optimal)

  * Time Complexity: **O(n)**
  * Space Complexity: **O(n)**

### Key Idea

Instead of searching for the second number every time, store previously seen numbers in a dictionary.

For each element:

1. Calculate the complement:

   ```
   complement = target - current_number
   ```
2. Check if the complement already exists in the dictionary.
3. If found, return the stored index and current index.
4. Otherwise, store the current number and its index.

---

## 💡 What I Learned

* A Hash Map stores data in **key → value** pairs.
* Python's `dict` is implemented using hashing.
* Hash Maps provide **O(1)** average lookup, insertion, and deletion.
* `dict.get(key, default)` simplifies frequency counting.
* Store **value → index** when solving lookup-based problems like Two Sum.
* Always check for the complement **before** inserting the current element.

---

## 🚀 Progress

* ✅ Learned Hash Map fundamentals
* ✅ Understood Dictionary operations
* ✅ Practiced frequency counting
* ✅ Solved Two Sum using Brute Force
* ✅ Optimized Two Sum using Hash Map

**Day 17/70 Complete ✅**
