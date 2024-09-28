'''
Leetcode 641 : Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4


'''


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