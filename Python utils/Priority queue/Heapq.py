
'''

In python we use heapq which is Priority queue
'''

import heapq

pq = []
p
# push
heapq.heappush(pq, 10)
heapq.heappush(pq, 5)
heapq.heappush(pq, 20)

# peek (smallest element)
print(pq[0])   # 👉 5

# pop (removes smallest)
print(heapq.heappop(pq))  # 👉 5

# heapq is empty of pq=[]

# -------------------------------------------------------------------------

#  To use max heap (use negative value)

import heapq

pq = []

heapq.heappush(pq, -10)
heapq.heappush(pq, -5)
heapq.heappush(pq, -20)

# peek max
print(-pq[0])   # 👉 20