'''
1381. Design a Stack With Increment Operation
Solved
Medium

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
 

Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.
 

Constraints:

1 <= maxSize, x, k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.

'''

class CustomStack:

    # Approach 1 : directly modifing the stack array with the incremeneted value .
    '''
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [-1]*maxSize 
        self.top=-1

    def push(self, x: int) -> None:
        if self.top+1<self.maxSize :
            self.top+=1
            self.stack[self.top]=x

    def pop(self) -> int:
        if self.top==-1:
            return -1
        element=self.stack[self.top]
        self.stack[self.top]=-1
        self.top-=1
        return element
        

    def increment(self, k: int, val: int) -> None:
        if k>self.top+1 :
            k=self.top+1
        
        for i in range(k):
            self.stack[i]+=val
        
    '''


    # Approach 2 :  Array using Lazy Propagation

    '''
    1) push ():
       - The push operation remains the same as before. No changes are needed in the incrementArray because pushing doesn't involve any increment adjustments.

    2) pop():

       - When popping an element, we return the value at the top of the stack, including any increments that apply to it. This is where  lazy propagation is used.

       - First, we retrieve the value at topIndex and add the corresponding increment from incrementArray. Since this top position is being removed, the increment for it needs to be passed down to the next element below. We do this by adding the increment at topIndex to incrementArray[topIndex-1], preserving the necessary increments for future pops.

       - Then, we decrement topIndex to remove the current top element.

    3) increment():
       - Instead of directly modifying the bottom k elements, we simply update the value at index k-1 in incrementArray. If the stack size is less than k, we update the increment at topIndex instead. This avoids unnecessary modifications and applies the increments only when the affected elements are accessed.

    '''
    def __init__(self, maxSize: int):
        self.inc =[0] * maxSize
        self.stack = [0] * maxSize
        self.top = -1
        

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x
        
        

    def pop(self) -> int:
        if self.top < 0:
            return -1
        result = self.stack[self.top] + self.inc[self.top]
        if self.top>0:
            self.inc[self.top - 1] += self.inc[self.top]
        self.inc[self.top] = 0
        self.top -= 1
        return result

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0:
            index = min(self.top, k-1)
            self.inc[index]  += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)