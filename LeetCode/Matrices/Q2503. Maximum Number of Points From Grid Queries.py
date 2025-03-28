'''
2503. Maximum Number of Points From Grid Queries
Solved
Hard

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106

'''
from heapq import heappush,heappop
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        '''
        step1 : sorting the queries (storing index of it)
        step2 : Initializing 
            -> res array of length len(queries)
            -> count , to count cells
            -> visit set ,initialised with origin 
            -> mean heap , that stores [grid[r][c],r,c]
        step4 : traversing through sorted queries
        step5 : While Loop , 
                Condition : 
                    -> checking if min_heap is empty or not 
                    -> val is greater than the heap[0][0]
                Body :
                    -> if heap[0][0] not in visited : pop() the element and count+=1
                    -> explore neighbours and push them to the queue
                    -> add count to the res array 
        step 6 : retun res array
        '''

        ROWS,COLS =len(grid),len(grid[0])

        q=[(n,i) for i,n in enumerate(queries)]
        q.sort()
        
        min_heap=[(grid[0][0],0,0)] # val,r,c
        visit=set([(0,0)])
        
        res = [0]* len(queries)
        count=0

        for limit,idx in q:
            while min_heap and min_heap[0][0] < limit :

                val,r,c=heappop(min_heap)
                count+=1
                neighbours=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
                for nr,nc in neighbours:
                    if ( 
                        0<=nr< ROWS and 0<=nc<COLS and 
                        (nr,nc) not in visit
                    ) :

                        heappush(min_heap,(grid[nr][nc],nr,nc))
                        visit.add((nr,nc))

            res[idx]=count
        return  res


        