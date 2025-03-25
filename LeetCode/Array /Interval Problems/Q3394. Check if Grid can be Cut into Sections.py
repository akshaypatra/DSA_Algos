'''

3394. Check if Grid can be Cut into Sections
Solved
Medium

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

 

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:



The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:



We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false

Explanation:

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.



'''

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        '''
        - Scan endpoints left to right
        - and top to down 
        - Similar to non overlapping intervals
        - Specifically 3 regions ?
        - Maybe ignore that and focus on overlapping
        - We just need atleast 3 non overlapping intervals

        '''
 
        x= [(r[0],r[2]) for r in rectangles] # (x1,x2)
        y= [(r[1],r[3]) for r in rectangles] # (y1,y2)

        x.sort()
        y.sort()

        def count_non_overlapping(intervals):
            count=0
            prev_end=-1
            for start,end in intervals:
                if prev_end <= start:
                    count+=1
                prev_end=max(end,prev_end)

            return count

        return max(
            count_non_overlapping(x),
            count_non_overlapping(y)
        ) >=3