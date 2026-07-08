# Day 18 - Hash Maps (Part 2)

## 📌 Topics Covered
- Hash Maps (Dictionary)
- Frequency Counting
- Character Mapping
- One-to-One Mapping

## ✅ Problems Solved

### 1. Ransom Note (LeetCode 383)
**Difficulty:** Easy

**Concepts Learned**
- Count character frequencies using a HashMap.
- Decrease the frequency after using a character.
- Return `False` when a required character is unavailable.

**Time Complexity:** O(m + n)

**Space Complexity:** O(k)
- `k` = number of distinct characters

---

### 2. Isomorphic Strings (LeetCode 205)
**Difficulty:** Easy

**Concepts Learned**
- Maintain a one-to-one mapping between two strings.
- Use two HashMaps to validate mappings in both directions.
- Prevent multiple characters from mapping to the same character.

**Time Complexity:** O(n)

**Space Complexity:** O(k)

---

## 💡 Key Learning

Although both problems use HashMaps, they solve different types of problems.

- **Ransom Note** → Frequency Counting
- **Isomorphic Strings** → One-to-One Character Mapping

Understanding the purpose of the HashMap is more important than memorizing the implementation.

---

## 📚 What I Learned Today

- Building frequency tables using dictionaries.
- Updating and decrementing character counts.
- Maintaining bidirectional mappings.
- Using `zip()` to iterate through two strings simultaneously.
- Recognizing when a problem requires counting versus mapping.

---

## 🚀 Progress

- ✅ Day 18 Complete
- ✅ Hash Maps (Part 2)
- ✅ 2 LeetCode Problems Solved
