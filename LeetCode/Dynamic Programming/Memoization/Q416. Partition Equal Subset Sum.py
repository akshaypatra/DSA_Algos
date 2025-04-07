'''
416. Partition Equal Subset Sum
Solved
Medium

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        '''
        using Memoization with recursion

        '''
        # if sum(nums)%2!=0 or len(nums)==1:
        #     return False
        
        # half=sum(nums)//2
        # nums.sort()

        # cache={} # i,remaining -> True or False

        # def helper(i,remaining):
        #     if (i, remaining) in cache:
        #         return cache[(i, remaining)]

        #     if i == len(nums) or nums[i] > remaining:
        #         cache[(i, remaining)] = False
        #         return False

        #     if remaining - nums[i] == 0:
        #         cache[(i, remaining)] = True
        #         return True


        #     include = helper(i + 1, remaining - nums[i])
        #     exclude = helper(i + 1, remaining)

        #     cache[(i, remaining)] = include or exclude

        #     return cache[(i, remaining)]
            
        
        # return helper(0,half)


        '''
        Solution 2 : using set 
        '''

        if sum(nums)%2!=0:
            return False
        
        dp=set()
        dp.add(0)

        target=sum(nums)//2

        for n in nums:
            new_dp=set()
            for t in dp:
                new_dp.add(t+n)
                new_dp.add(t)
            dp=new_dp
        return True if target in dp else False
        
            


        


        
