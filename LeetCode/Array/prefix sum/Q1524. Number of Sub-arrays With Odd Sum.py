'''

1524. Number of Sub-arrays With Odd Sum
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100

'''

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Define a large number for modulo operation to prevent integer overflow
        mod = 10**9 + 7
      
        # Initialize the count of subarrays with even and odd sum
        count = [1, 0]  # Even sums are initialized to 1 due to the virtual prefix sum of 0 at the start
      
        # Initialize answer and prefix sum variables
        answer = 0
        prefix_sum = 0
      
        # Iterate over the array elements
        for num in arr:
            # Update the prefix sum
            prefix_sum += num
          
            # Increment the answer by the number of subarrays encountered so far
            # that when added to the current element yields an even sum
            answer = (answer + count[prefix_sum % 2 ^ 1]) % mod
          
            # Update the count of subarrays with current sum parity
            count[prefix_sum % 2] += 1
          
        # Return the final answer
        return answer