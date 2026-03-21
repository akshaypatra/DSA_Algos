'''
Priority Queue using Queue and Heapdict module in Python
Last Updated : 8 Jan, 2026
A Priority Queue is a special type of queue where elements with higher priority are dequeued before elements with lower priority. If two elements have the same priority, they are served according to their order in the queue.

Let's learn how to use Priority Queue in Python with queue.PriorityQueue and heapdict.

Using queue.PriorityQueue
queue.PriorityQueue is a constructor to create a priority queue, where items are stored in priority order (lower priority numbers are retrieved first).

Functions:

put(): Puts an item into the queue.
get(): Removes and returns an item from the queue.
qsize(): Returns the current queue size.
empty(): Returns True if the queue is empty, False otherwise. It is equivalent to qsize()==0.
full(): Returns True if the queue is full, False otherwise. It is equivalent to qsize()>=maxsize.


'''

from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, 'g'))
pq.put((3, 'e'))
pq.put((4, 'k'))
pq.put((5, 's'))
pq.put((1, 'e'))


print(pq)
print(pq.get())
print(pq.get())  

print('Items in queue:', pq.qsize())
print('Is queue empty:', pq.empty())
print('Is queue full:', pq.full())

