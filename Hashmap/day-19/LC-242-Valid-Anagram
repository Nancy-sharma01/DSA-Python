class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count={}
        if len(s) != len(t):
            return False

        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for letter in t:
            if letter not in count or count[letter]==0:
                return False
            # if letter in count: No need bcz not in vali condition satitisfies only
            count[letter]-=1
        return True
