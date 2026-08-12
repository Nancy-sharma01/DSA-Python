# Day 26 - Evaluate Reverse Polish Notation

## 📌 Problem Solved
**150. Evaluate Reverse Polish Notation (Medium)**

### 🧠 Topic
- Stack
- Expression Evaluation
- Simulation

### 🚀 Approach
- Used a stack to evaluate the Reverse Polish (Postfix) expression.
- Traversed each token in the input.
- If the token was a number, pushed it onto the stack.
- If the token was an operator:
  - Popped the top two operands.
  - Applied the operator while maintaining the correct operand order.
  - Pushed the result back onto the stack.
- Used integer arithmetic to ensure division truncates toward zero without floating-point precision issues.
- The final value remaining in the stack is the answer.

### 💡 Key Learning
- Reverse Polish Notation evaluates expressions without parentheses using a stack.
- Operand order is crucial for subtraction and division.
- Integer division should truncate toward zero, not floor the result.
- Avoid floating-point division for large integers to prevent precision loss.

### ⏱️ Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

### 🎯 Status
✅ Accepted on LeetCode
