class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ch = {}

        for letter in magazine:
            if letter in ch:
                ch[letter] += 1
            else:
                ch[letter] = 1

        for letter in ransomNote:
            if letter not in ch or ch[letter] == 0:
                return False

            ch[letter] -= 1

        return True
