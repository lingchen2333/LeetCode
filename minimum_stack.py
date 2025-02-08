from collections import deque


class MinStack:
    # keep a stack of current min value
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else: 
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin() # return 0
minStack.pop()
minStack.top()    # return 2
minStack.getMin() # return 1
  
