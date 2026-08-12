class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The second operand is popped first
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if (a < 0) != (b < 0):
                        stack.append(-(-a // b))
                    else:
                        stack.append(a // b)
            else:
                stack.append(int(token))
                
        return stack[0]
