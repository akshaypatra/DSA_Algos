'''
594. Longest Harmonious Subsequence
Solved
Easy

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

 

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109

'''



class Solution:
    def findLHS(self, nums: List[int]) -> int:

        '''
        Solution 1 : Using Counter(hashmap)

        -> more optimized

        '''
        # c=Counter(nums)
        # k=list(c.keys())
        # k.sort()
        # max_count=0

        # for i in range(len(k)-1):
        #     if k[i+1]-k[i]==1:
        #         max_count=max(max_count,c[k[i+1]]+c[k[i]])
        # return max_count



        '''
        Solution 2 : sorting and sliding window

        '''

        nums.sort()
        start = 0
        max_len = 0
        
        for end in range(len(nums)):
            while nums[end] - nums[start] > 1:
                start += 1
            if nums[end] - nums[start] == 1:
                max_len = max(max_len, end - start + 1)
        
        return max_len





            