'''
Leetcode 179 : Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # Not optimised but works
        # nums.sort()

        # if set(nums)=={0}:
        #    return "0"

       

        # def helper(a,b):

        #     if int(a+b) > int(b+a):
        #         return 1
        #     else:
        #         return -1
        
        # for j in range(len(nums)):
        #     for i in range(len(nums)-1):
        #         if helper(str(nums[i]),str(nums[i+1]))==1:
        #             continue
        #         else :
        #             nums[i],nums[i+1]=nums[i+1],nums[i]
        
        # s=""
        # for i in nums:
        #     s+=str(i)
        # return s



        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)
        
