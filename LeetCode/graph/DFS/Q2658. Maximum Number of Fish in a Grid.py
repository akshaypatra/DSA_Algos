'''

2658. Maximum Number of Fish in a Grid
Solved
Medium

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10

'''

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        '''

        # All test case passed

        ROWS=len(grid)
        COLS=len(grid[0])
        res=0

        def dfs(r,c,visit):

            if (r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            lres=grid[r][c]

            neighbours=[(r, c + 1), (r, c - 1), (r + 1, c) , (r - 1, c)]
            for nr,nc in neighbours:
                lres += dfs(nr, nc, visit)
                
            
            return lres 
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    res=max(dfs(r,c,set()),res)
        
        return res

        '''

        # OPTIMISED CODE (minimal changes that makes much more of diffrence in time complexity)

        def dfs(r,c):
            if (r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]==0 or visit[r][c] ) :
                return 0
            
            visit[r][c]=True
            res=grid[r][c]

            neighbours=[(r, c + 1), (r, c - 1), (r + 1, c) , (r - 1, c)]
            for nr,nc in neighbours:
                res += dfs(nr, nc)

            return res



        ROWS=len(grid)
        COLS=len(grid[0])

        res=0
        visit=[[False]* COLS for _ in range(ROWS)] # Using visted grid (similar to hashset)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] or visit[r][c]:
                    res=max(dfs(r,c),res)
        
        return res
