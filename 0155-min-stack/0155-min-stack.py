class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else:
            mini = min(self.stack[-1][1],val)
            self.stack.append([val,mini])
        

    def pop(self) -> None:
        if not self.stack:
            return -1
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1][0]

        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()