'''

1726. Tuple with Same Product
Solved
Medium

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

'''

import math
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        '''

        Bruteforce approach (all test case passed)
        

        Intuition : 
        ->take product of every element with every other element and increment the value to the product(as key)
        ->if pair of elements exceeds 2 then multiply number of pairs with 8 to get total number of combinations
        -> using combination formula C(n,2) to calculate number of combinations of pair

        Time Complexity :
        -> O(n^2)

        Space Complexity :
        -> O(1)

        '''

        # def total_pairs(n):

        #     # combinations of forming a pair 
        #     '''
        #     pairs=0
        #     for i in range(1,n):
        #         pairs+=i
        #     return pairs
        #     '''

        #     '''
        #     using C(n,k)=n!/k1(n-k)!
        #     '''

        #     # return int(math.factorial(n)/(math.factorial(2)*math.factorial(n-2)))

        #     #shortcut of C(n,2) is n(n-1)//2
        #     return (n*(n-1))//2



        # d=defaultdict(int)

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         d[nums[i]*nums[j]]+=1
        

        # count=0
        # for i in d.keys():
        #     if d[i]>=2:
        #         count+=total_pairs(d[i])*8

        # return count


        '''

        Optimised code 
        -> O(n^2) time complexity

        '''


        d=defaultdict(int)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                d[nums[i]*nums[j]]+=1
        

        count=0
        for i in d.keys():
            if d[i]>=2:
                count+=((n*(n-1))//2)*8

        return count






        
