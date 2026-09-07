class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[None]*maxSize
        self.maxSize=maxSize
        self.top=-1
        

    def push(self, x: int) -> None:
        if self.top< self.maxSize-1:
            self.top+=1
            self.stack[self.top]=x
        
        

    def pop(self) -> int:
        if self.top == -1:
            return -1
        val = self.stack[self.top] 
        self.stack[self.top] = 0
        self.top -= 1
        return val

        

    def increment(self, k: int, val: int) -> None:
        limit = min(k, self.top + 1)  # Increment up to the top or k elements
        for i in range(limit):
            self.stack[i] += val
        

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)