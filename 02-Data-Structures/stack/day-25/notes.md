# Day 25 Notes – Stack (Part 3)

## Problem 1: LC 71 – Simplify Path

### Idea

Treat each folder as an element in a stack.

* Ignore `""` and `"."`
* Pop when `".."` is encountered (if possible)
* Push valid directory names
* Join the remaining directories to form the simplified path

### Algorithm

1. Split the path using `'/'`.
2. Traverse each part.
3. Ignore empty strings and `"."`.
4. Pop the stack for `".."` if it's not empty.
5. Push valid folder names.
6. Return the canonical path using `"/".join(stack)`.

### Important Python Functions

```python
path.split('/')
```

Splits the path into directory names.

```python
stack.append(folder)
```

Pushes a directory.

```python
stack.pop()
```

Moves to the parent directory.

```python
"/".join(stack)
```

Creates the final path.

### Common Mistakes

* Using `list(path)` instead of `path.split('/')`
* Forgetting to ignore empty strings
* Using `=` instead of `==`
* Using `push()` instead of `append()`
* Using `split()` instead of `join()` while returning the answer

---

# Problem 2: LC 155 – Min Stack

### Goal

Support all operations in constant time:

* Push
* Pop
* Top
* Get Minimum

### Key Observation

Store both the value and the minimum up to that point.

Instead of storing:

```text
5
2
7
1
```

Store:

```text
(5,5)
(2,2)
(7,2)
(1,1)
```

Each tuple remembers the minimum when it was pushed.

### Operations

**Push**

* If the stack is empty, store `(value, value)`.
* Otherwise:

  * Retrieve the previous minimum.
  * Compute `min(value, previous_min)`.
  * Store `(value, current_min)`.

**Pop**

Remove the last tuple.

**Top**

Return the first element of the top tuple.

**GetMin**

Return the second element of the top tuple.

### Why This Works

Every element remembers the minimum up to its position.

After a pop operation, the new top already stores the correct minimum.

No extra traversal is required.

### Complexity

| Operation | Time |
| --------- | ---- |
| Push      | O(1) |
| Pop       | O(1) |
| Top       | O(1) |
| GetMin    | O(1) |

Space Complexity: `O(n)`

---

# Today's Learning

* Stack is useful beyond simple push and pop problems.
* Additional information can be stored inside a stack element to optimize future operations.
* Tuples are a clean way to associate multiple values with each stack entry.
* Carefully handling edge cases prevents runtime errors and incorrect outputs.

---

## Day 25 Reflection

Today's session focused on understanding the reasoning behind stack-based solutions instead of simply implementing them. The biggest lesson was learning to design a data structure by storing extra information with each element, allowing all operations to run efficiently in constant time. This approach is a common interview pattern and strengthened my confidence in solving design-oriented DSA problems.
