'''
2078. Two Furthest Houses With Different Colors
Solved
Easy

There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

 

Example 1:


Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.
Example 2:


Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
Example 3:

Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
 

Constraints:

n == colors.length
2 <= n <= 100
0 <= colors[i] <= 100
Test data are generated such that at least two houses have different colors.
'''

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        '''
        Approach 1 : Bruteforce 

        TC : O(n^2)
        SC : O(n)
        '''

        # max_distance=0

        # for i in range(len(colors)-1):
        #     for j in range(i+1,len(colors)):
        #         if colors[i]!=colors[j]:
        #             max_distance = max( max_distance , j-i )
        # return max_distance

        '''
        Approach 2 : Greedy Approach : Forward and Backward Scan

        - Thus, we can use the first house (left end), or the last house (right end) and find the farthest house from it with a
         different color.

        - If we scan inward from the opposite side of each end, the first mismatch already gives the farthest possible house for that
         end.

        '''

        n = len(colors)
        left, right = 0, n - 1

        for i in range(n):
            if colors[i] ^ colors[-1]:
                left = i
                break

        for i in range(n - 1, -1, -1):
            if colors[i] ^ colors[0]:
                right = i
                break

        return max(n - 1 - left, right)
