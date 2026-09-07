'''
3356. Zero Array Transformation II
Solved
Medium

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 5 * 105
1 <= queries.length <= 105
queries[i].length == 3
0 <= li <= ri < nums.length
1 <= vali <= 5

'''

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        #Time limit exceeded
        '''
        count=0
        if set(nums)=={0}:
            return 0

        for i,j,v in queries:
            for k in range(i,j+1):
                if v>=nums[k]:
                    nums[k]-=nums[k]
                else:
                    nums[k]-=v
            count+=1
            if set(nums)=={0}:
                break

        if set(nums)!={0}:
            return -1  
        return count 
        '''

        def check(k: int) -> bool:
            # Initialize a difference array with an extra element for boundary management
            difference_array = [0] * (len(nums) + 1)
          
            # Apply each query's effect to the difference array
            for left, right, value in queries[:k]:
                difference_array[left] += value
                difference_array[right + 1] -= value
          
            # Accumulate the changes from the difference array
            accumulated_sum = 0
            for original_value, change in zip(nums, difference_array):
                accumulated_sum += change
                # Check if the accumulated value can zero out the original array value
                if original_value > accumulated_sum:
                    return False
            return True

        # Determine the number of queries
        num_queries = len(queries)
      
        # Use binary search to find the minimum number of queries needed
        l = bisect_left(range(num_queries + 1), True, key=check)
      
        # Return -1 if not possible, otherwise return the minimum queries needed
        return -1 if l > num_queries else l
                