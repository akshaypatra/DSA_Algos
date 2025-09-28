'''
976. Largest Perimeter Triangle
Solved
Easy

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
 

'''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        '''
        Bruteforce Solution 

        '''
        # n=len(nums)
        # max_p=0
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]>nums[k] and nums[i]+nums[k]>nums[j]  and nums[k]+nums[j]>nums[i]:
        #                 max_p=max(max_p,nums[i]+nums[j]+nums[k])
        # return max_p

        '''
        Using sorting and 
        '''
        nums.sort()
        n=len(nums)
        i=n-3
        j=n-2
        k=n-1
        while i>=0:
            if nums[i]+nums[j]>nums[k] and nums[i]+nums[k]>nums[j]  and nums[k]+nums[j]>nums[i]:
                return nums[i]+nums[j]+nums[k]
            i-=1
            k-=1
            j-=1

        return 0