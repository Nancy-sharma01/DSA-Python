"""
LeetCode 238 - Product of Array Except Self

Concepts:
- Prefix Products
- Arrays
- Precomputation

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        answer = [0] * n

        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer
