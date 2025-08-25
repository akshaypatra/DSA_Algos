'''

498. Diagonal Traverse
Solved
Medium

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows, num_cols = len(matrix), len(matrix[0])
      
        diagonal_order = []
      
        # There will be (num_rows + num_cols - 1) diagonals to cover in the matrix.
        for k in range(num_rows + num_cols - 1):
          
    
            temp = []
          
            # Calculate the starting row index. It is 0 for the first 'num_cols' diagonals,
            # otherwise we start at an index which goes down from 'num_rows - 1'.
            row = 0 if k < num_cols else k - num_cols + 1
          
            # Calculate the starting column index. It is 'k' for the first 'num_cols' diagonals,
            # otherwise we start at 'num_cols - 1' and go down.
            col = k if k < num_cols else num_cols - 1
          
            # Fetch the elements along the current diagonal.
            # Continue while 'row' is within the matrix row range and 'col' is non-negative.
            while row < num_rows and col >= 0:
                temp.append(matrix[row][col])
                row += 1  # Move down to the next row.
                col -= 1  # Move left to the next column.
          
            # Reverse every other diagonal's elements before appending it to the result list
            # to get the right order.
            if k % 2 == 0:
                temp = temp[::-1]
          
            # Extend the main result list with the elements of the current diagonal.
            diagonal_order.extend(temp)
      
        # Return the final result list.
        return diagonal_order