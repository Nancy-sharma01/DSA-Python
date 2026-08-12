# Day 25 - Stack (Part 3)

## 📚 Problems Solved

### ✅ LeetCode 71 - Simplify Path (Medium)

* Used a stack to simulate Unix file system navigation.
* Ignored `"."` (current directory) and empty strings.
* Used `".."` to move back by popping from the stack.
* Constructed the final canonical path using `"/".join(stack)`.

**Concepts Learned**

* Stack simulation
* String splitting and parsing
* Path normalization
* Handling edge cases

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)`

---

### ✅ LeetCode 155 - Min Stack (Medium)

* Designed a stack supporting `push`, `pop`, `top`, and `getMin` in **O(1)** time.
* Stored tuples `(value, current_min)` to keep track of the minimum element at every level.
* Retrieved the minimum instantly from the top tuple without traversing the stack.

**Concepts Learned**

* Stack design
* Tuples in Python
* Data structure optimization
* Constant time retrieval

**Time Complexity**

* Push → `O(1)`
* Pop → `O(1)`
* Top → `O(1)`
* GetMin → `O(1)`

**Space Complexity:** `O(n)`

---

## 🚀 Key Takeaways

* Not every stack problem is about matching brackets. Stacks can also simulate navigation and help design efficient data structures.
* Storing additional information with each stack element can eliminate expensive computations later.
* Understanding *why* a solution works is more valuable than memorizing code.

---

## 📈 Progress

**Day 25/70 Completed ✅**

Another day, another step closer to becoming interview-ready. 💪
