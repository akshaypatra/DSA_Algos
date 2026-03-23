'''
1594. Maximum Non Negative Product in a Matrix
Solved
Medium

You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
Example 3:


Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4

'''

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        '''
        DP Solution : Maintain min and maximum product

        -> create dp_min and dp_max array of m*n size 
        -> dp_min contains minimum product till now 
        -> dp_max conatins maximum product till now

        -> fill the dp_min and dp_max array with 1st row products and 1st column products

        -> traverse the grid (0from 2 row and 2 column)
            -> if the current element is positive - (as positive * positive maked graeter number)
                    - extract element from upper and left element from dp_max 
                    - dp_max[i][j]= grid[i][j] * max (dp_max[i-1][j] , dp_max[i][j-1])
            ->. if the current element grid[i][j] is negative -  (as neg and neg no. makes great positive number)
                    - extract element form upper and left elementfrom dp_min
                    - dp_min[i][j] = grid[i][j] * min (dp_min[i-1][j] , dp_min[i][j-1])

        -> return the dp_max[i][j]

        '''

        ROWS , COLS = len(grid) , len(grid[0])

        dp_max = [[0]*COLS for _ in range(ROWS)] # to track maximum product 
        dp_min = [[0]*COLS for _ in range(ROWS)] # to track minimum product

        dp_max[0][0] = dp_min[0][0] = grid[0][0] # initialising with grid[0][0]

        # Filling 1st ROW with rightward product
        for j in range(1,COLS):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1]*grid[0][j]

        # Filling 1st COl with the downward product
        for i in range(1,ROWS):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0]*grid[i][0]

        for i in range(1,ROWS):
            for j in range(1,COLS):
                val = grid[i][j]

                candidates = [
                    # maximum elements
                    dp_max[i-1][j]*val , #upper element of val in maximum
                    dp_max[i][j-1]*val , #left element of val in maximum

                    #minimum elements
                    dp_min[i-1][j]*val , # upper element of  val in minimum
                    dp_min[i][j-1]*val , # left element of  val in minimum
                ]

                # maintaining max and min product till now
                dp_max[i][j]=max(candidates)
                dp_min[i][j]=min(candidates)
        
        res = dp_max[ROWS-1][COLS-1]

        return res%(10**9 +7) if res>=0 else -1




