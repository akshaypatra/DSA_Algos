'''
73. Set Matrix Zeroes
Solved
Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        Bruteforce approach : works 
        '''

        # ROWS=len(matrix)
        # COLS=len(matrix[0])

        # rows=set()
        # cols=set()
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j]==0:
        #             rows.add(i)
        #             cols.add(j)

        # for i in range(ROWS):
        #     if i in rows:
        #         matrix[i]=[0]*COLS
            
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if j in cols:
        #             matrix[i][j]=0


        '''
        Optimized solution
        '''

        ROWS=len(matrix)
        COLS=len(matrix[0])

        rows=set()
        cols=set()
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)

        for i in range(ROWS):
            if i in rows:
                matrix[i]=[0]*COLS
            else:
                for j in range(COLS):
                    if j in cols:
                        matrix[i][j]=0

            
        
        
            


        

                
        
        