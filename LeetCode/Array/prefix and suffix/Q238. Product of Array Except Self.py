'''

238. Product of Array Except Self
Solved
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        PREFIX POSTFIX approach
        Intuition : initialising a prefix array and a postfix array

        [a,b,c,d]

        prefix=[1,a,a*b,a*b*c]
        postfix=[b*c*d,c*d,d,1]

        '''

        '''
        N=len(nums)
    

        pre=[1]*N
        post=[1]*N

        for i in range(1,N):
            pre[i]*=pre[i-1]*nums[i-1]
        
        for j in range(N-2,-1,-1):
            post[j]*=post[j+1]*nums[j+1]
        
        
        for k in range(N):
            nums[k]=pre[k]*post[k]
        
        return nums

        '''



        '''

        optimisation : removing postfix array and maintain a postfix variable to calculate postfix and multipkly it to the 
                        prefix of the element .

        -> beats 94 %

        '''

        res=[1]*len(nums)

        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res



