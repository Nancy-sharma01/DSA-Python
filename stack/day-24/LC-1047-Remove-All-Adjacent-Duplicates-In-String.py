class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            # If the stack is not empty and the current character 
            # matches the top of the stack, remove the duplicate pair
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # Otherwise, push the character onto the stack
                stack.append(char)
                
        # Join the remaining characters in the stack to form the final string
        return "".join(stack)
