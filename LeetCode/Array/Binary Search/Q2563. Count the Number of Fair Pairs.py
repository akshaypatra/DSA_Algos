'''
2563. Count the Number of Fair Pairs
Solved
Medium

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109

'''

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:


        '''

        Two Pointer approach  with binary search

        '''

        def bin_search(l,r,target):
            

            while l<=r:
                m=(l+r)//2
                if nums[m]>=target:
                    r=m-1
                else:
                    l=m+1

            return r

            
                    
        nums.sort()
        res=0

        for i in range(len(nums)):

            low=lower-nums[i]
            up=upper-nums[i]

            res+=(
                bin_search(i+1,len(nums)-1,up+1) - 
                bin_search(i+1,len(nums)-1,low)
            )
        return res


        
    

        '''
        bruteforce approach 

        -> TC : O(n^2) : Time Limit exceeded
        '''

        # count=0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if lower<=nums[i]+nums[j] and nums[i]+nums[j]<=upper :
        #             count+=1
                
        # return count


