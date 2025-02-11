'''

15. 3Sum
Solved
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        '''
        Two pointer approach
        -> O(nlogn) + O(n^2) = O(n^2)

        '''

        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):  
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements for i
                continue
            
            # Similar to two sum
            l, r = i + 1, n - 1  
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  # Skip duplicates for p2
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:  # Skip duplicates for p3
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res




        

        '''

        Bruteforce solution 2

        -> O(n^2)
        -> 308 / 313 testcases passed

        '''
        # nums.sort()
        # res=[]

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         remaining=0-nums[i]-nums[j]
        #         if remaining in nums[j+1:] and ([nums[i],nums[j],remaining ] not in res):
        #             res.append([nums[i],nums[j],remaining])
        # return res


        '''
        Bruteforce solution
        -> 308 / 313 testcases passed
        -> O(n^3)

        '''

        # nums.sort()
        # res=[]
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0 and ([nums[i],nums[j],nums[k]] not in res) :
        #                 res.append([nums[i],nums[j],nums[k]])
        # return  res