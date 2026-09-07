
'''
Using Two Queues : Always keep the newest element at the front of one queue.

    q1: []
    q2: [3,2,1]

'''


from collections import deque
class MyStack:
    
    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:

        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1 #swap
        

    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return not self.q1


'''
Using only one queue : After pushing a new element, rotate the queue so that the newest element comes to the front.

'''
from collections import deque

class StackUsingOneQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q

