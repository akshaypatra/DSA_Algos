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
        # nums.sort()
        # max_element=nums[0]
        # max_count=1

        # cur_count=1
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[i-1]:
        #         if cur_count >= max_count :
        #             max_count = cur_count
        #             max_element = nums[i-1]
        #         cur_count = 1
        #     else :
        #         cur_count += 1
        # if cur_count > max_count :
        #     max_count = cur_count
        #     max_element = nums[i-1]

        # return max_element


        '''
        Approach 3 : Majority element  algorithm
        TC : O(n)
        SC : O(1)

        We use the same idea of approach 1 above but actually, we don't have to use HashMap.
        We use two variables res and majority.

        ⭐️ Points

            - res is return value.
            - majority is frequency of majority number(= res).
            - Every time current number is the same as res, we add +1 to majority. If not, we add -1 to majority.
            - When majority is 0, it's time to change majority number(= res), because every time current number and res are different,
            we add -1 to majority, so if majority is 0, that means a current majority number(= res) is not the majority number anymore
            That's why when majority is 0, update res with current number.
        '''
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res