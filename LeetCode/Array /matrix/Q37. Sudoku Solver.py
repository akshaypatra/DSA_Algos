'''
37. Sudoku Solver
Solved
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves a Sudoku puzzle using backtracking.
        Modifies the board in-place.
        """
        def backtrack(index):
            """
            Recursively fill empty cells using DFS backtracking.
          
            Args:
                index: Current index in the empty_cells list
            """
            nonlocal solved
          
            # Base case: all empty cells have been filled successfully
            if index == len(empty_cells):
                solved = True
                return
          
            # Get the current empty cell's position
            row_idx, col_idx = empty_cells[index]
          
            # Try each digit from 1 to 9
            for digit in range(9):
                # Check if placing digit+1 is valid in current position
                if (not row_used[row_idx][digit] and 
                    not col_used[col_idx][digit] and 
                    not block_used[row_idx // 3][col_idx // 3][digit]):
                  
                    # Mark the digit as used in row, column, and 3x3 block
                    row_used[row_idx][digit] = True
                    col_used[col_idx][digit] = True
                    block_used[row_idx // 3][col_idx // 3][digit] = True
                  
                    # Place the digit on the board
                    board[row_idx][col_idx] = str(digit + 1)
                  
                    # Recursively solve for the next empty cell
                    backtrack(index + 1)
                  
                    # If solution found, stop backtracking
                    if solved:
                        return
                  
                    # Backtrack: undo the current placement
                    row_used[row_idx][digit] = False
                    col_used[col_idx][digit] = False
                    block_used[row_idx // 3][col_idx // 3][digit] = False
      
        # Initialize tracking arrays for used digits
        # row_used[i][d] = True if digit d+1 is used in row i
        row_used = [[False] * 9 for _ in range(9)]
        # col_used[j][d] = True if digit d+1 is used in column j
        col_used = [[False] * 9 for _ in range(9)]
        # block_used[bi][bj][d] = True if digit d+1 is used in block (bi, bj)
        block_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]
      
        # List to store positions of empty cells
        empty_cells = []
      
        # Flag to indicate if solution is found
        solved = False
      
        # Initialize the board state and collect empty cells
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == '.':
                    # Record empty cell position
                    empty_cells.append((row_idx, col_idx))
                else:
                    # Mark existing digits as used
                    digit = int(board[row_idx][col_idx]) - 1
                    row_used[row_idx][digit] = True
                    col_used[col_idx][digit] = True
                    block_used[row_idx // 3][col_idx // 3][digit] = True
      
        # Start solving from the first empty cell
        backtrack(0)
        