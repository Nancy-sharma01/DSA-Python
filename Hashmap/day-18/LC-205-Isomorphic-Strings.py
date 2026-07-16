class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST = {}
        mapTS = {}

        for s_char, t_char in zip(s, t):

            if s_char in mapST:
                if mapST[s_char] != t_char:
                    return False

            if t_char in mapTS:
                if mapTS[t_char] != s_char:
                    return False

            mapST[s_char] = t_char
            mapTS[t_char] = s_char

        return True
