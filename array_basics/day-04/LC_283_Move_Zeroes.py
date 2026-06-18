"""
LeetCode 283 - Move Zeroes

Approach:
- Use a pointer k to track the position where the next non-zero element should be placed.
- Traverse the array and move all non-zero elements to the front.
- After placing all non-zero elements, fill the remaining positions with zeroes.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        Do not return anything, modify nums in-place instead.
        """

        k = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # Fill the remaining positions with zeroes
        while k < len(nums):
            nums[k] = 0
            k += 1
