# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        
        el = self.stack.pop()
        
        if el == self.min[-1]:
            self.min.pop()
        
        return el

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min:
            return None
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

