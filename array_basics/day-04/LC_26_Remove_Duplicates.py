"""
LeetCode 26 - Remove Duplicates from Sorted Array

Approach:
- Since the array is sorted, duplicates will be adjacent.
- Use a pointer k to track the position of the next unique element.
- Traverse the array starting from index 1.
- If the current element is different from the previous unique element,
  place it at index k and increment k.
- Return k as the count of unique elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Handle edge case
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
