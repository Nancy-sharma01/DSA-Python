# LC 1480 - Running Sum of 1D Array | Day 03 | Arrays
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
