"""
LeetCode 27 - Remove Element

Approach:
- Use a pointer k to track the position where the next valid element should be placed.
- Traverse the array.
- If the current element is not equal to val, place it at index k.
- Increment k.
- Return k as the new length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
