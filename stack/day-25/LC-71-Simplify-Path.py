class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        parts=path.split('/')
        for ch in parts:
            if ch=='.'or not ch:
                continue
            elif ch=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/" + "/".join(stack)
