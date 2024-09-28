class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[None] * k
        self.f,self.r = -1,-1
        self.k=k

     
    # Insert Operations

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.f,self.r=0,0
            self.deque[self.f]=value
        elif self.isFull():
            return False
        elif self.f==0:
            self.f=self.k-1
            self.deque[self.f]=value
        else:
            self.f-=1
            self.deque[self.f]=value
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.f,self.r=0,0
            self.deque[self.f]=value

        elif self.isFull():
            return False
        elif self.r==self.k-1:
            self.r=0
            self.deque[self.r]=value
        else:
            self.r+=1
            self.deque[self.r]=value
        return True



    # Display Operation

    def display(self):
        i=self.f
        while i!=self.r:
            print(self.deque[i])
            i=(i+1)%self.k
        print(self.deque(self.r))

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.f==self.r:
            self.f,self.r=-1,-1
        elif self.f==self.k-1:
            self.f=0
        else:
            self.f+=1
        return True
        


    # Delete Operations

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.f==self.r:
            self.f,self.r=-1,-1
        elif self.r==0:
            self.r=self.k-1
        else:
            self.r-=1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.f]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.r]
        

    def isEmpty(self) -> bool:
        if (self.f==-1 and self.r==-1):
            return True
        return False

    def isFull(self) -> bool:
        if (self.f==0 and self.r==self.k-1) or (self.f==self.r+1):
            return True
        return False
    

   
    
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()