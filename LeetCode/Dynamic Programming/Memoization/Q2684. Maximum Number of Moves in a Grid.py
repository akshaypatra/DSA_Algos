'''

2684. Maximum Number of Moves in a Grid
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

 

Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106

'''


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])        

        cache = {}

        def helper(r, c):
            # Base case: if we reached the rightmost column, no further moves can be made
            if c == COLS - 1:
                return 0

            # Check if the result for this cell is already in the cache
            if (r, c) in cache:
                return cache[(r, c)]

            # Explore possible moves
            max_moves = 0
            # Move up-right
            if r > 0 and c + 1 < COLS and grid[r][c] < grid[r - 1][c + 1]:
                max_moves = max(max_moves, 1 + helper(r - 1, c + 1))
            # Move right
            if c + 1 < COLS and grid[r][c] < grid[r][c + 1]:
                max_moves = max(max_moves, 1 + helper(r, c + 1))
            # Move down-right
            if r + 1 < ROWS and c + 1 < COLS and grid[r][c] < grid[r + 1][c + 1]:
                max_moves = max(max_moves, 1 + helper(r + 1, c + 1))

            # Cache the result for this cell
            cache[(r, c)] = max_moves
            return max_moves

        # Start from any cell in the first column and find the max moves
        result = 0
        for r in range(ROWS):
            result = max(result, helper(r, 0))

        return result
        

        
