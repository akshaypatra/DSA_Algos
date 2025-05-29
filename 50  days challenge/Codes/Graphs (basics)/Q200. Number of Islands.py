'''
200. Number of Islands
Solved
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        '''
        My implimentation

        -> logic is correct

        Issues :
        -> islands dictionary is useless
        -> used recursion instead of queue
        -> redundant condition checking 

        '''
        # ROWS=len(grid)
        # COLS=len(grid[0])
        # islands=defaultdict(list)

        # visited=set()
        # def bfs(r,c,island):
        #     if (r,c) in visited:
        #         return 
        #     if grid[r][c]=="1":
        #         islands[island].append((r,c))
        #         visited.add((r,c))
        #         neighbours=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        #         for nr,nc in neighbours:
        #             if 0<=nr<ROWS and 0<=nc<COLS and ( (nr,nc) not in visited ) and grid[nr][nc]=="1":
        #                 islands[island].append((nr,nc))
        #                 visited.add((nr,nc))
        #                 bfs(nr,nc,island)
        #     return 
        
        # island=1
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c]=="1" and (r,c) not in visited :
        #             bfs(r,c,island)
        #             island+=1
        # return len(islands)

        '''

        corrected version with  optimization

        '''

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            while queue:
                row, col = queue.pop(0)
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        return count



