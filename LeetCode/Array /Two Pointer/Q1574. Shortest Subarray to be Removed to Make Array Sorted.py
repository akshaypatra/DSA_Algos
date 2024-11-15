'''

1574. Shortest Subarray to be Removed to Make Array Sorted
Solved
Medium
Topics
Companies
Hint
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.


'''

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        # Step 1: Find the longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the whole array is non-decreasing
        if left == n - 1:
            return 0
        
        # Step 2: Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Step 3: Initialize the minimum length to remove
        min_to_remove = min(n - left - 1, right)
        
        # Step 4: Try to merge prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                min_to_remove = min(min_to_remove, j - i - 1)
                i += 1
            else:
                j += 1
        
        return min_to_remove



            