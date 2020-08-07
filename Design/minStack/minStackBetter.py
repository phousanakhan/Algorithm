class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        return self.list.append((x, curMin))
        
    def pop(self) -> None:
        self.list.pop()        

    def top(self) -> int:
        return self.list[-1][0]
        

    def getMin(self) -> int:
        #if len(self.list) == 0:
        #if self.list == None or self.list == []:
        if len(self.list) == 0:
            return None
        else:
            return self.list[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
