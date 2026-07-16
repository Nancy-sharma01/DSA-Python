class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map_ps = {}
        map_sp = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for p_char, word in zip(pattern, words):
            if p_char in map_ps:
                if map_ps[p_char] != word:
                    return False

            elif word in map_sp:
                if map_sp[word] != p_char:
                    return False
            else:
                map_ps[p_char]=word
                map_sp[word]=p_char
        return True
                

