'''
69. Majority Element
Solved
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        '''
        approach 1 : hashmap/hashset 
            - count the frequency 
            - check which element occurs more than n/2

        TC : O(n)
        SC : O(n)
        '''
        # n=len(nums)
        # c=Counter(nums)
        # for i in c.keys():
        #     if c[i]>=n//2+1:
        #         return i
        # return -1


        '''
        Approach 2 : Sorting and counting max_element.

        TC : O(n)
        SC : O(1)
        '''
        nums.sort()
        max_element=nums[0]
        max_count=1

        cur_count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if cur_count >= max_count :
                    max_count = cur_count
                    max_element = nums[i-1]
                cur_count = 1
            else :
                cur_count += 1
        if cur_count > max_count :
            max_count = cur_count
            max_element = nums[i-1]

        return max_element
