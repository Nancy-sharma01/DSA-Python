# Day 23 - Stack (Introduction)

## 📌 Topic
- Stack (LIFO - Last In First Out)

## 🧠 Concepts Learned
- What is a Stack?
- LIFO Principle
- Stack Operations:
  - Push
  - Pop
  - Peek
  - isEmpty
- Implementing a Stack using Python List
- Using Dictionary + Stack together
- Handling edge cases while working with stacks

## ✅ Problem Solved

### LeetCode 20 - Valid Parentheses
**Difficulty:** Easy

### Approach
- Used a stack to keep track of opening brackets.
- Used a dictionary to map closing brackets to their corresponding opening brackets.
- For every opening bracket, pushed it onto the stack.
- For every closing bracket:
  - Checked whether the stack was empty.
  - Compared the top element of the stack with the expected opening bracket.
  - Popped if matched; otherwise returned `False`.
- At the end, returned `True` only if the stack was empty.

## ⏱️ Time Complexity
- **O(n)**

## 💾 Space Complexity
- **O(n)**

## 🎯 Outcome
- Learned the fundamentals of Stack.
- Understood how stacks help solve bracket matching problems.
- Successfully solved LeetCode 20: Valid Parentheses.
