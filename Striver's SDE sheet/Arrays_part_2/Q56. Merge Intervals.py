'''
56. Merge Intervals
Solved
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        '''   
        Example 1 : [[1,3],[2,6],[8,10],[15,18]]

        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

        1---3
          2-------6
                      8---10
                                         15-------18

        Result :

        1---------6   8---10             15-------18


        Example 2 :[[1,4],[4,5]]

        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

        1-----4
              4-5
        
        Result :

        1-------5

        '''

        if len(intervals)==1:
            return intervals

        intervals.sort()
        result=[intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0]<=result[-1][1]:
                
                result[-1][1]=max(intervals[i][1],result[-1][1])

            else :
                result.append(intervals[i])
        
        return result

        





