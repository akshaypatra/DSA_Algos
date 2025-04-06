'''

368. Largest Divisible Subset
Solved
Medium

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        Intution : memoization (2 parameter)

        '''

        # nums.sort()
        # cache={} # (i,prev)-> []

        # def dfs(i,prev):
        #     if i==len(nums):
        #         return []
        #     if (i,prev) in cache:
        #         return cache[(i,prev)]
            
        #     res=dfs(i+1,prev)
        #     if nums[i] % prev==0:
        #         tmp=[nums[i]]+dfs(i+1,nums[i])
        #         res=tmp if len(tmp) >len(res) else res

        #     cache[(i,prev)]=res
        #     return res
        # return dfs(0,1)

        '''
        Memoization : memory efficient solution

        cache[i] = longest starting at i , and including nums[i]
        '''
        nums.sort()
        cache={}

        def dfs(i):
            if i ==len(nums) : return []
            if i in cache:return cache[i]

            res=[nums[i]]
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    tmp=[nums[i]]+dfs(j)
                    if len(tmp)>len(res):
                        res=tmp
            cache[i]=res
            return res
        
        res=[]
        for i in range(len(nums)):
            tmp=dfs(i)
            if len(tmp)>len(res):
                res=tmp
        return res








    

        