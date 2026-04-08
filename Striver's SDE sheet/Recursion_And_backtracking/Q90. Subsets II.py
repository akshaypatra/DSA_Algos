'''
90. Subsets II
Solved
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        '''
        Algorithm : Skip and backtrack 

            Sort array (to group duplicates - easy to skip)
            Start with empty subset
            At each step → add subset to result
            Loop from current index
            Skip duplicates
            Pick element → go deeper → backtrack

        '''

        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res