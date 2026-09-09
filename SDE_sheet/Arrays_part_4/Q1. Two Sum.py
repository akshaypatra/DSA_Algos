'''
1. Two Sum
Solved
Easy

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Approach : Two pointer

        -> sort the nums in ascending order 
        -> p1 at index 0 
        -> p2 at index len(nums)-1
        -> if nums[p1] + nums[p2] > target , then decrement p2 
        -> if nums[p1] + nums[p2] < target , then increment p1
        -> return the p1 and p2 if nums[p1]+nums[p2]==target

        TC : O(n)
        SC : O(nlogn)

        '''

        for i in range(len(nums)):
            nums[i]=(nums[i],i)

        nums.sort()
        p1=0
        p2=len(nums)-1

        while p1<p2:
            if nums[p1][0]+nums[p2][0]==target:
                return [nums[p1][1],nums[p2][1]]
            elif nums[p1][0]+nums[p2][0]>target:
                p2-=1
            else :
                p1+=1
        return []
