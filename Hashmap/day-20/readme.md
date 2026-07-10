# Day 20 - Hashing | Grouping & Cycle Detection

## 🎯 Goal
Strengthen Hash Map and Hash Set concepts by solving problems involving grouping anagrams and detecting cycles.

---

## 📚 Topics Covered
- Hash Maps (Dictionaries)
- Hash Sets
- Grouping by Signature
- Sorting as a Hash Key
- Simulation
- Cycle Detection

---

## ✅ Problems Solved

### 1. LeetCode 49 - Group Anagrams (Medium)

**Concepts:**
- Hash Map
- Grouping by Signature
- Sorting
- Tuples as Dictionary Keys

**Approach:**
- Sort each word alphabetically to create a unique signature.
- Convert the sorted characters into a tuple so it can be used as a dictionary key.
- Store all words with the same signature in the same list.
- Return all grouped lists.

**Time Complexity:** `O(n × k log k)`

- `n` = number of strings
- `k` = maximum length of a string

**Space Complexity:** `O(n × k)`

---

### 2. LeetCode 202 - Happy Number (Easy)

**Concepts:**
- Hash Set
- Simulation
- Cycle Detection

**Approach:**
- Repeatedly replace the number with the sum of the squares of its digits.
- Store every visited number in a Hash Set.
- If the number becomes `1`, it is a Happy Number.
- If a number repeats, a cycle is detected, so return `False`.

**Time Complexity:** `O(log n)` per iteration

**Space Complexity:** `O(log n)`

---

## 💡 Key Learnings

- A sorted word can act as a unique **signature** for grouping anagrams.
- Tuples are immutable and can be used as dictionary keys.
- Hash Maps are useful for grouping related data efficiently.
- Hash Sets are an excellent choice for detecting repeated states and cycles.
- Using a temporary variable preserves the original value while processing digits.

---

## 🧠 Patterns Learned

- **Group by Signature** (Hash Map)
- **Simulation + Cycle Detection** (Hash Set)

These are common interview patterns and appear in many medium-level problems.

---

## 🚀 Progress

- ✅ Day 20 Completed
- ✅ Problems Solved Today: **2**
- 🟢 Easy: **1**
- 🟡 Medium: **1**
- 🔥 DSA Challenge Progress: **20 / 75 Days**

---

