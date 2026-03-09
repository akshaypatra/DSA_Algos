'''
Kaden's Algorithm 

To find the maximum sum of a contiguous subarray.
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

'''

def maxSubArray(nums):
    maxSum = nums[0]
    curSum=0

    for i in nums:
        if curSum<0:
            curSum=0
        curSum+=i
        maxSum = max(maxSum , curSum)
    return maxSum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


