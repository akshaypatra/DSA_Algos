'''
1582. Special Positions in a Binary Matrix
Solved
Easy

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        '''
        Approach : Row and column count

        -> initialize  two arrays :
            1. row_count of len(mat) size
            2. col_count of len(mat[0]) size

        -> when the element is 1 , increment the count of 1 
            a) in i th index of row_count and 
            b) jth index of col_count
        
        -> check for value 1 in row_count and col_count ( in one of them ) and increment the result

        -> return the result 
        '''


        ROWS = len(mat)
        COLS = len(mat[0])

        row_count = [0]*(ROWS)
        col_count = [0]*(COLS)

        total_count = 0 

        for row in range(ROWS) :
            for col in range(COLS) :
                if mat[row][col]==1 :
                    row_count[row]+=1
                    col_count[col]+=1
        
        for row in range (ROWS) :
            for col in range(COLS) :
                if mat[row][col]==1 :
                    if row_count[row]==1 and col_count[col]==1 :
                        total_count+=1
        
        return total_count
