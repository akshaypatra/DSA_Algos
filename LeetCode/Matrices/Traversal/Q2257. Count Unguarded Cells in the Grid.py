'''

2257. Count Unguarded Cells in the Grid
Solved
Medium

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

'''

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # FIRST TRY
        
        # matrix=[[0] * n for _ in range(m)]

        # # visited=set()

        # for i,j in walls:
        #     matrix[i][j]=2
        
        # for i,j in guards:
        #     # north direction
        #     if i>0 :
        #         p1=i
        #         p2=j
        #         while p1>0  :
        #             p1=p1-1
        #             if matrix[p1][p2]!=2:
        #                 # visited.add([p1,p2])
        #                 matrix[p1][p2]=1
        #             else:
        #                 break
                
        #     # south direction 
        #     if i<m-1 :
        #         p1=i
        #         p2=j
        #         while p1<m-1  :
        #             p1=p1+1
        #             if matrix[p1][p2]!=2:
        #                 # visited.add([p1,p2])
        #                 matrix[p1][p2]=1
        #             else:
        #                 break
            
        #     # west  direction
        #     if j>0:
        #         p1=i
        #         p2=j
        #         while p2>0:
        #             p2=p2-1
        #             if matrix[p1][p2]!=2:
        #                 # visited.add([p1,p2])
        #                 matrix[p1][p2]=1
        #             else:
        #                 break

        #     # east direction
        #     if j<n-1:
        #         p1=i
        #         p2=j
        #         while p2<n-1:
        #             p2=p2+1
        #             if matrix[p1][p2]!=2:
        #                 # visited.add([p1,p2])
        #                 matrix[p1][p2]=1
        #             else:
        #                 break
        # count=0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #             count+=1
        # return count
            
        # Second Trye

        
        matrix = [[0] * n for _ in range(m)]

        # Mark walls with 2
        for i, j in walls:
            matrix[i][j] = 2
        
        # Mark guards with 3
        for i, j in guards:
            matrix[i][j] = 3

        # Function to mark cells in a specific direction
        def mark_guarded(x, y, dx, dy):
            while 0 <= x < m and 0 <= y < n:
                if matrix[x][y] == 2 or matrix[x][y] == 3:  
                    break
                if matrix[x][y] == 0:  # Mark unguarded cells as guarded
                    matrix[x][y] = 1
                x += dx
                y += dy

        
        for i, j in guards:
            # Mark north
            mark_guarded(i - 1, j, -1, 0)

            # Mark south
            mark_guarded(i + 1, j, 1, 0)

            # Mark west
            mark_guarded(i, j - 1, 0, -1)
            
            # Mark east
            mark_guarded(i, j + 1, 0, 1)

        # Count unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    count += 1

        return count

            

            
            

        

        
