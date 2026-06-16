# Day 02 - Time Complexity Examples

# -------------------------

# O(1) - Constant Time

# -------------------------

def get_first_element(arr):
return arr[0]

# -------------------------

# O(n) - Linear Time

# -------------------------

def print_elements(arr):
for element in arr:
print(element)

# -------------------------

# O(n²) - Quadratic Time

# -------------------------

def print_pairs(arr):
for i in arr:
for j in arr:
print(f"({i}, {j})")

# -------------------------

# Testing the Functions

# -------------------------

numbers = [1, 2, 3, 4, 5]

print("===== O(1) Example =====")
print("First Element:", get_first_element(numbers))

print("\n===== O(n) Example =====")
print_elements(numbers)

print("\n===== O(n²) Example =====")
print_pairs([1, 2, 3])
