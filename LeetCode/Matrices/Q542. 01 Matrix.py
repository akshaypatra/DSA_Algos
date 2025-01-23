'''

542. 01 Matrix
Solved
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        '''

        # 18/50 test case 

        ROWS=len(mat)
        COLS=len(mat[0])

        visit=set()

        for r in range(ROWS):
            for c in range(COLS):

                if mat[r][c]==1:

                    minimum_cost=float("inf")
                    neighbours=[[r,c-1],[r,c+1],[r+1,c],[r-1,c]]
                    for nr,nc in neighbours:
                        if nr<0 or nc<0 or nr==ROWS or nc==COLS or (nr,nc)  in visit:
                            continue
                        
                        minimum_cost=min(minimum_cost,mat[nr][nc])
                    
                    mat[r][c]+=minimum_cost
                    visit.add((r,c))
        return mat
        ''' 

        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()
        visit = set()
        
        # Step 1: Initialize queue with all `0` cells
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))  # Store (row, col, distance)
                    visit.add((r, c))
                else:
                    mat[r][c] = float('inf')  # Mark `1`s as unvisited

        # Step 2: Perform BFS
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                    mat[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))
                    visit.add((nr, nc))  # Mark as visited
        
        return mat    
                        

        