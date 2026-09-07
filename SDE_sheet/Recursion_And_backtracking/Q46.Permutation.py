'''
46. Permutations
Solved
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Approach 1: Recursion 

        TC : O(n^2)
        SC : O(n) 
        '''
        # res=[]
        # def helper(l):

        #     # base condition 
        #     if len(l)==len(nums):

        #         res.append(l)
        #         return
            
        #     for i in range(len(nums)):
        #         if nums[i] not in l:
        #             helper(l+[nums[i]])
            
            
             
        # for i in range(len(nums)):
        #     helper([nums[i]])
        
        # return res

        '''
        Approach 2 : backtracking  and visited_array 
        Optimization : using visited array  instead of if nums[i] in l
        TC : O(n^2)
        SC : O(n) 
        '''
        res = []
        visited = [False]*len(nums)   
        def backtrack(path):

            # base condition 
            if len(path)==len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue
                
                
                # Choose the ith value
                visited[i]=True
                path.append(nums[i])

                # Explore
                backtrack(path)

                # Do_not choose the path (backtrack)
                path.pop()
                visited[i]=False
                    
                
        backtrack([])
        return res

