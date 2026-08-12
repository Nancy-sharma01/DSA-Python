# ============================================================
# Day 02 - Time Complexity Examples in Python
# Concepts: O(1), O(log n), O(n), O(n²), Space Complexity
# ============================================================


# ── 1. O(1) - Constant Time ──────────────────────────────────
# Number of operations stays the same regardless of input size

def get_first_element(arr):
    """Returns the first element of the array — always 1 operation."""
    return arr[0]

def get_last_element(arr):
    """Returns the last element of the array — always 1 operation."""
    return arr[-1]


# ── 2. O(log n) - Logarithmic Time ───────────────────────────
# Input is halved at each step — Binary Search is the classic example

def binary_search(arr, target):
    """Searches for target in a sorted array using Binary Search.
    Time Complexity: O(log n) — halves the search space each step.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid          # target found, return index
        elif arr[mid] < target:
            left = mid + 1      # search right half
        else:
            right = mid - 1     # search left half

    return -1                   # target not found


# ── 3. O(n) - Linear Time ────────────────────────────────────
# Operations grow linearly with input size

def print_elements(arr):
    """Prints every element in the array — visits each once."""
    for element in arr:
        print(element, end=" ")
    print()

def find_max(arr):
    """Finds the maximum element by scanning the full array.
    Time Complexity: O(n) — checks every element once.
    """
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


# ── 4. O(n²) - Quadratic Time ────────────────────────────────
# Nested loops — grows quadratically with input size

def print_pairs(arr):
    """Prints all pairs from the array using nested loops."""
    for i in arr:
        for j in arr:
            print(f"({i}, {j})", end=" ")
        print()

def bubble_sort(arr):
    """Sorts array using Bubble Sort.
    Time Complexity: O(n²) — compares every pair of elements.
    """
    n = len(arr)
    arr = arr.copy()            # don't modify original
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ── 5. Space Complexity ───────────────────────────────────────
# O(1) space — no extra memory used

def sum_array(arr):
    """Returns sum of array elements.
    Time: O(n) | Space: O(1) — only one variable used.
    """
    total = 0
    for num in arr:
        total += num
    return total

# O(n) space — extra memory grows with input

def copy_array(arr):
    """Returns a copy of the array.
    Time: O(n) | Space: O(n) — new array of same size created.
    """
    return [x for x in arr]


# ── Testing All Functions ─────────────────────────────────────

numbers = [1, 2, 3, 4, 5]
sorted_numbers = [1, 3, 5, 7, 9, 11, 15]   # must be sorted for binary search

print("===== O(1) Example =====")
print("First Element:", get_first_element(numbers))   # Output: 1
print("Last Element:", get_last_element(numbers))      # Output: 5

print("\n===== O(log n) Example =====")
index = binary_search(sorted_numbers, 7)
print("Index of 7:", index)                            # Output: 3
print("Index of 6:", binary_search(sorted_numbers, 6)) # Output: -1 (not found)

print("\n===== O(n) Example =====")
print("Elements:", end=" ")
print_elements(numbers)                                # Output: 1 2 3 4 5
print("Max Value:", find_max(numbers))                 # Output: 5

print("\n===== O(n²) Example =====")
print("All Pairs:")
print_pairs([1, 2, 3])
# Output:
# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)

unsorted = [64, 34, 25, 12, 22]
print("Bubble Sorted:", bubble_sort(unsorted))         # Output: [12, 22, 25, 34, 64]

print("\n===== Space Complexity Example =====")
print("Sum:", sum_array(numbers))                      # Output: 15
print("Copy:", copy_array(numbers))                    # Output: [1, 2, 3, 4, 5]
