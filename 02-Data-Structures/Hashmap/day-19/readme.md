# Day 19 - Hashing Practice

## 🎯 Goal
Strengthen understanding of **Hash Maps (Dictionaries)** by solving classic hashing problems on LeetCode.

---

## 📚 Topics Covered
- Hash Maps (Dictionaries)
- Frequency Counting
- One-to-One (Bijective) Mapping
- String Manipulation

---

## ✅ Problems Solved

### 1. Word Pattern (Easy)
**Concepts:**
- Two Hash Maps
- Bijective Mapping
- String Splitting

**Approach:**
- Split the input string into words.
- Check if the number of words matches the pattern length.
- Maintain two dictionaries:
  - Pattern → Word
  - Word → Pattern
- Verify both mappings remain consistent throughout the traversal.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

---

### 2. Valid Anagram (Easy)
**Concepts:**
- Hash Map
- Frequency Counting

**Approach:**
- Check if both strings have the same length.
- Count the frequency of each character in the first string.
- Traverse the second string and decrement the corresponding counts.
- If a character is missing or its count becomes invalid, return `False`.
- Otherwise, the strings are valid anagrams.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

---

## 💡 Key Learnings
- A **single Hash Map** is enough when only character frequencies need to be compared.
- **Two Hash Maps** are required when maintaining a one-to-one (bijective) relationship between two sets of values.
- Always validate simple edge cases (like length mismatch) before processing.
- Small implementation mistakes (variable names, missing conditions) can cause incorrect results even when the algorithm is correct.

---

## 🚀 Progress
- ✅ Day 19 Completed
- ✅ Hashing Practice
- ✅ LeetCode Problems Solved Today: 2

---
*"Consistency beats intensity. Every problem solved today is one step closer to becoming interview-ready."*
