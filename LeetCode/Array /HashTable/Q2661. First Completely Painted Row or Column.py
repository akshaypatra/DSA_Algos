'''

2661. First Completely Painted Row or Column
Solved
Medium

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].

'''

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS,COLS = len(mat),len(mat[0])

        mat_to_position={} # n-> (r,c)

        for r in range(ROWS):
            for c in range(COLS):
                mat_to_position[mat[r][c]]=(r,c)

        row_cnt=[0]*ROWS
        col_cnt=[0]*COLS

        for i in range(len(arr)):
            r,c=mat_to_position[arr[i]]

            row_cnt[r]+=1
            col_cnt[c]+=1

            if row_cnt[r]==COLS or col_cnt[c]==ROWS :
                return i