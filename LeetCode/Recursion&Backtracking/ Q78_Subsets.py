# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]

        def helper(nums,temp,i):

            # base case
            if i==len(nums):
                self.ans.append(temp[:])  #note : we append a copy of temp variable to avoid the changes made on it affterwards
                return
            
            # inclusion of nums[i]
            temp.append(nums[i])
            helper(nums,temp,i+1)
            temp.pop() #backtrack

            # exclusion of nums[i]
            helper(nums,temp,i+1)

            return



        helper(nums,[],0)
        return self.ans