'''

2342. Max Sum of a Pair With Equal Sum of Digits
Solved
Medium

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109


'''

from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        '''

        Intuition : 
        -> store elements in hashset having same digit_sum
        -> finding two max elements which has same digit sum.

        Time Complexity :
        -> O(n)

        Space Complexity :
        -> O(logn)

        '''



        hashset=defaultdict(list) # digit_sum -> [elements]

        for i,n in enumerate(nums):
            s=0
            for digit in str(n):
                s+=int(digit)
            hashset[s].append(n)

        max_sum=-1
        for k in hashset.keys():
            l=hashset[k]
            if len(l)>=2:
                l.sort()
                max_sum=max(max_sum,l[-1]+l[-2]) #getting 2 max elements 
        return max_sum


