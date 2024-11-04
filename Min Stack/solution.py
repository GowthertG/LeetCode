class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            tmp = self.stack.pop()
            if tmp == self.minStack[-1]:
                self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        

obj = MinStack()
obj.push(-5)
obj.push(1)
obj.push(3)
obj.push(3)
obj.push(1)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(5)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3 )
print(param_4 )
