'''
128. Longest Consecutive Sequence
Solved
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Approach 1 : Sorting and counting 

        TC : O(nlogn)  SC :O(1)

        '''

        '''
        Approach 2 : Set and next look up 

        -> create a set for O(1) lookup
        -> traverse through each elements of nums
            - assume the current index as the start of the sequence if its prev (num-1) doen't exist 
            - nowlook for next number in sequence from the set
            - if exist increment the sequence_counter and move to next number in the set
            - do this till the next number doesn't exist in the set .
        -> take the max of each sequence and store it in res
        -> return res
        '''


        s = set(nums) # O(1) look up
        res = 0

        for num in s :
            # check if its start of sequence
            if num-1 not in s :
                length = 0
                while num+length in s :
                    length +=1

                res = max(res,length)
        return res

 
