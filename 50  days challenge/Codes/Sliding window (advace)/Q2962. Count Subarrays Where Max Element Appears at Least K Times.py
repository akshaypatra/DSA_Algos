'''

2962. Count Subarrays Where Max Element Appears at Least K Times
Solved
Medium

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105

'''

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """

        subarray -> Sliding window
        

        """

        m=max(nums)
        res=0
        left=0
        count=0
        for right in range(len(nums)):
            if nums[right]==m:
                count+=1
                        
            
            while left<=right and count>=k:
                # res+=len(nums)-right
                if nums[left]==m:
                    count-=1
                left+=1
            res+=left
        return res