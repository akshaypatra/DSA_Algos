'''
812. Largest Triangle Area                             
Easy                          

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:
                                                              

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: poin          ts = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.

'''

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        '''
        Formula used  : Gauss's area 

        Area = 0.5 * [ x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) ]
        '''
        max_area = 0
        n = len(points)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    cur_area = 0.5 * abs(
                        points[i][0] * (points[j][1] - points[k][1]) +
                        points[j][0] * (points[k][1] - points[i][1]) +
                        points[k][0] * (points[i][1] - points[j][1])
                    )
                    max_area = max(max_area, cur_area)

        return max_area