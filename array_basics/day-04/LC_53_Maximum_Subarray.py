"""
LeetCode 53 - Maximum Subarray

Approach (Kadane's Algorithm):
- Keep track of the maximum subarray sum ending at the current index.
- At each element, decide whether to:
  1. Start a new subarray from the current element, or
  2. Extend the existing subarray.
- Update the global maximum sum during traversal.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
