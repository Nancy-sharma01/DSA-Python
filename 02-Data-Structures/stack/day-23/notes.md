# Day 23 Notes - Stack

# What is a Stack?

A Stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

Example:

Stack of Plates

        ┌──────┐
Top --->│ Plate│
        ├──────┤
        │ Plate│
        ├──────┤
        │ Plate│
        └──────┘

The last plate placed on the top is the first one removed.

---

# Stack Operations

## Push
Adds an element to the top of the stack.

Python:
```python
stack.append(x)
```

Time Complexity:
O(1)

---

## Pop

Removes the top element.

```python
stack.pop()
```

Time Complexity:

O(1)

---

## Peek (Top)

Returns the top element without removing it.

```python
stack[-1]
```

Time Complexity:

O(1)

---

## Check Empty

```python
len(stack) == 0
```

or

```python
not stack
```

---

# Implementing Stack in Python

Python does not require a separate Stack class for DSA.

We use a list.

```python
stack = []
```

Push

```python
stack.append(10)
```

Pop

```python
stack.pop()
```

Peek

```python
stack[-1]
```

---

# Why Stack?

Stacks are useful whenever the most recently added element needs to be processed first.

Common Applications:

- Valid Parentheses
- Browser Back Button
- Undo / Redo
- Function Calls
- Expression Evaluation
- Depth First Search (DFS)
- Backtracking

---

# Valid Parentheses Pattern

Dictionary

```python
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

Algorithm:

1. Create an empty stack.
2. Traverse the string.
3. If opening bracket:
   - Push onto stack.
4. If closing bracket:
   - If stack is empty → False
   - If top matches expected opening bracket → Pop
   - Otherwise → False
5. At the end:
   - Empty stack → True
   - Non-empty stack → False

---

# Important Learning

A Stack is not a different Python data type.

A Python list behaves like a stack when we use only:

- append()
- pop()

The data structure remains a list, but the behavior follows the Stack (LIFO) principle.

---

# Mistakes I Made Today

- Compared a character with the entire dictionary.
- Initially mapped opening brackets to closing brackets instead of the reverse.
- Forgot to check if the stack was empty before accessing `stack[-1]`.
- Missed handling the mismatch case.
- Forgot to verify that the stack was empty after processing all characters.

Debugging these mistakes helped me understand the algorithm instead of memorizing it.

---

# Key Takeaways

- Stack stores recently opened brackets.
- Dictionary helps identify the expected opening bracket.
- Always check if the stack is empty before accessing the top.
- Every push should eventually have a matching pop.
- A valid parentheses string leaves the stack empty at the end.

---

Day 23 Complete ✅
