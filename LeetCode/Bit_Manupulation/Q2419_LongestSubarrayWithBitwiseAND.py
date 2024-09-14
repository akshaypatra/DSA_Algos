'''
Leetcode 2419 : Longest subarray with maximum bitwise AND 

You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

'''

# SOLUTION


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        '''
        Used maximum number streak algo as  bitwise AND will be always greater for greates number
        '''
        # target =max(nums)
        # size,res=0,0

        # for n in nums:
        #     if n==target:
        #         size+=1
        #     else:
        #         size=0
        #     res=max(res,size)
        # return res

    
        # SOLUTION 2

        #  1. If n<cur_max , n & cur_max < cur_max
        #  2. If n==cur_max , n & cur_max = cur_max
        #  3. If n>cur_max , n & cur_max < cur_max

        size,res=0,0
        cur_max=0
        for n in nums:
            if n > cur_max:
                cur_max = n
                size =1
                res=0
            elif n==cur_max:
                size+=1
            else:
                size=0
            res=max(res,size)
        return res