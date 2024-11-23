'''

1861. Rotating the Box
Solved
Medium
Topics
Companies
Hint
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 


'''

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # r=len(box)
        # c=len(box[0])

        # matrix=[[0]*r for _ in range(c)]

        # for i in range(r):
        #     for j in range(c):
        #         matrix[j][i]=box[i][j]
        
        # for i in range(r-1,-1,-1):
        #     p1=c-1
        #     p2=c-2
        #     while p2>-1:
        #         if matrix[p1][i]=="." and matrix[p2][i]=="#":
        #             temp=matrix[p1][i]
        #             matrix[p1][i]=matrix[p2][i]
        #             matrix[p2][i]=temp
        #             p1-=1
        #             p2-=1
        #         elif matrix[p1][i]=="." and matrix[p2][i]==".":
        #             p2-=1
               
        #         else:
        #             p1-=1
        #             p2-=1
        # return matrix
        
        r = len(box)
        c = len(box[0])

        # Simulate gravity for each row in the box
        for i in range(r):
            empty_pos = c - 1  # Start from the last column
            for j in range(c - 1, -1, -1):
                if box[i][j] == '#':  # Stone found
                    box[i][j], box[i][empty_pos] = box[i][empty_pos], box[i][j]
                    empty_pos -= 1
                elif box[i][j] == '*':  # Obstacle found
                    empty_pos = j - 1  # Reset empty_pos to the left of the obstacle

        # Rotate the box clockwise
        rotated_box = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                rotated_box[j][r - i - 1] = box[i][j]

        return rotated_box
                

