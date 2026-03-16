'''
74. Search a 2D Matrix
Solved
Medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Approach 1 : Binary Search on 2d matrix
        '''

        # def binary_search(array):
        #     low=0
        #     high = len(array)-1

        #     while low <= high :

        #         mid=low + (high-low)//2

        #         if array[mid]==target :
        #             return True
                
        #         elif target<array[mid] :
        #             high=mid-1
        #         else :
        #             low=mid+1
        #     return False


        # low = 0
        # high = len(matrix)-1

        # while low<=high :

        #     mid=low+ (high-low)//2

        #     if matrix[mid][0]<=target<=matrix[mid][-1]:
        #         return binary_search(matrix[mid])
        #     elif target < matrix[mid][0] :
        #         high=mid-1
        #     else :
        #         low=mid+1
        # return False


        '''
        Approach 2. : top-right corner elimination strategy:
        (more effecient)-O(log(m * n))
        1. Starting position: Begin at top-right corner (row=0, col=n-1)
        2. Target found: If current element equals target, return true
        3. Move down: If target > current, eliminate current row (move down: i++)
        4. Move left: If target < current, eliminate current column (move left: j--)
        5. Boundary termination: Stop when we go out of bounds (no valid position remains)
        '''

        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False