'''
3446. Sort Matrix by Diagonals
Solved
Medium

You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:



The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

 

Constraints:

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105

'''

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''

        [00 01 02]
        [10 11 12]
        [20 21 22]

        '''



        ROWS=len(grid)
        COLS =len(grid[0])



        p1=ROWS-1
        p2=0


        alt_mat=[]

        while 0<=p1<ROWS  and 0<=p2<COLS:

            cur_d=[]

            i=p1
            j=p2

            while 0<=i<ROWS and 0<=j<COLS:
                cur_d.append(grid[i][j])
                i+=1
                j+=1
            if p1>=p2:
                cur_d.sort(reverse=True)
            else:
                cur_d.sort()
            
            if p1>0:
                p1-=1
            else:
                p2+=1

            alt_mat.extend(cur_d)
        


        res_mat=[[-1 for _ in range(ROWS)] for _ in range(COLS) ]


        counter=0

        p1=ROWS-1
        p2=0

        while 0<=p1<ROWS  and 0<=p2<COLS:

            i=p1
            j=p2

            while 0<=i<ROWS and 0<=j<COLS:
                res_mat[i][j]=alt_mat[counter]
                counter+=1
                i+=1
                j+=1
           
            
            if p1>0:
                p1-=1
            else:
                p2+=1


        return res_mat


