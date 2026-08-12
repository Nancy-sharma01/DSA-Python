# 🚀 DSA Challenge - Day 14

## 📌 Topic
Sliding Window (Fixed Size)

---

## ✅ Problem Solved

1. LeetCode 643 - Maximum Average Subarray I (Easy)

---

## 💡 Concepts Learned

- Sliding Window Technique
- Fixed Size Window
- Window Sum Optimization
- Time Complexity Improvement
- Python Division Difference (Python vs Python3)

---

## 🧠 Key Takeaway

Instead of calculating the sum of every subarray repeatedly, Sliding Window updates the current sum by adding the incoming element and removing the outgoing element.

```python
current_sum += nums[i] - nums[i - k]
```

This makes the solution run in **O(n)** time.

---

## 📊 Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

---

## 🎯 Progress

- ✅ Day 14 Completed
- ✅ Sliding Window Started
- ✅ 1 LeetCode Problem Solved

---
