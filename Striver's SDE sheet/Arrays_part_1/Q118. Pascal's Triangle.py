'''
118. Pascal's Triangle
Solved
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal_triangle = [[1]]
      

        for i in range(1, numRows):
  
            new_row = [1]

            for j in range(1, i):
                sum_of_elements = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
                new_row.append(sum_of_elements)
          

            new_row.append(1)
          
            pascal_triangle.append(new_row)

        return pascal_triangle

