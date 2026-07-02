# 🚀 Day 13 – String Compression (LC 443)

## 📅 Challenge Progress

* **Day:** 13 / 70
* **Topic:** Strings (Day 4)
* **Problem Solved:** LC 443 – String Compression *(Medium)*

---

## 🧠 Problem Summary

Given an array of characters, compress it **in-place** by replacing consecutive repeating characters with the character followed by its count. If a character appears only once, it remains unchanged. Return the new length of the compressed array.

---

## 🎯 Key Concepts Learned

* Two Pointer Technique

  * `read` pointer to traverse the original array.
  * `write` pointer to overwrite the array with the compressed result.
* Counting consecutive characters.
* In-place array modification.
* Converting integer counts into individual characters using `str(count)`.

---

## ⚡ Approach

1. Traverse the array using a **read** pointer.
2. Count consecutive occurrences of the current character.
3. Write the character once using the **write** pointer.
4. If the count is greater than 1, write each digit of the count.
5. Return the final value of the **write** pointer as the new length.

---

## ⏱ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## 💡 What I Learned Today

* How to solve in-place array problems using separate **read** and **write** pointers.
* Why two pointers are useful when the output size differs from the input size.
* How to process groups of consecutive characters efficiently.
* The importance of dry-running an algorithm before coding.

---

## 🌱 Reflection

Today's problem was challenging at first because understanding the problem statement took some time. After breaking it down and tracing the algorithm step by step, the two-pointer approach became much clearer. This problem strengthened my understanding of in-place modifications and improved my confidence with medium-level string problems.

---
