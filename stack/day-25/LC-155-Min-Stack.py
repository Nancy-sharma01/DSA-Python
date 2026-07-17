class MinStack(object):
    
    def __init__(self):
        self.obj=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.obj:
            current_min=value
            self.obj.append((value,current_min))
        else:
            previous_min =  self.obj[-1][1]

            current_min = min(value, previous_min)

            self.obj.append((value, current_min))
        

    def pop(self):
        """
        :rtype: None
        """
        self.obj.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.obj[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.obj[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
