class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check= set(nums)
        pt=0
        count=0
        longest=0
        for num in check:
            if num-1 not in check:
                pt= num
                count=1
                while pt+1 in check:
                    pt+=1
                    count+=1
            longest= max(longest,count)
        return longest
