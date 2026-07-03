class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            # Add the next element and remove the first element of the previous window
            current_sum += nums[i] - nums[i - k]
            # Track the maximum sum found so far
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Return the maximum average
        return float (max_sum) / k
