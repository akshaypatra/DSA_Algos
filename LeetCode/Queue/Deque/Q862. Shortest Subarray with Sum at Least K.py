'''

862. Shortest Subarray with Sum at Least K
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109

'''

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        result = float('inf')

        for i in range(n + 1):
            # Remove elements from the deque front if the condition is met
            while dq and prefix[i] - prefix[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Maintain the monotonicity of the deque
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            # Add the current index to the deque
            dq.append(i)

        return result if result != float('inf') else -1