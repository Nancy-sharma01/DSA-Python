class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group={}
        
        for word in strs:
            char_tuple_key=tuple(sorted(word))
            if char_tuple_key in group:
                group[char_tuple_key].append(word)
            else:
                group[char_tuple_key] = [word]
        return list(group.values())
