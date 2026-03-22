'''
1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
'''

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
       
            '''
            90 degree rotation means :
                - transpose -> reverse

                0   1   2         --->      0   1   2
            0   00  01  02         90*  0   20  10  00
            1   10  11  12              1   21  11  01
            2   20  21  22              2   22  12  11
            

            so we have to do rotation 3 times and  and check if target matches or not

            '''


        
            def rotate(matrix):
                n = len(matrix)

                # transpose
                for i in range(n):
                    for j in range(i + 1, n):
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                # reverse rows
                for row in matrix:
                    row.reverse()

            # Try all 4 rotations
            for _ in range(4):
                if mat == target:
                    return True
                rotate(mat)

            return False




