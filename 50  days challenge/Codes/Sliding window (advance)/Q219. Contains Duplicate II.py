'''
219. Contains Duplicate II
Solved
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
     
        # Bruteforce : O(n^2) -Time limit exceeded

        '''
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True

        return False
        '''


        # Using hashtable : O(nlogn) -Not that efficient , but worked


        '''
        h=defaultdict(list)
        for i in range(len(nums)):
            h[nums[i]].append(i)
        

        for i in h.keys():
            if len(h[i])>=2:
                for e in range(len(h[i])-1):
                    if abs(h[i][e]-h[i][e+1])<=k:
                        return True
        return False
        '''

        # using Sliding Window

        '''
        Window size : k
        '''

        # if len(nums) <= 1:
        #     return False

        # h = defaultdict(int)
        # p1 = 0
        # p2 = 0

        # while p2 < len(nums):
        #     if h[nums[p2]] >= 1:
        #         return True

        #     h[nums[p2]] += 1
        #     if p2 - p1 >= k:
        #         h[nums[p1]] -= 1
        #         p1 += 1

        #     p2 += 1

        # return False
    
        # More optimized

        seen = {}
        for i, val in enumerate(nums):
            if val in seen and abs(i-seen[val]) <= k:
                return True
            else:
                seen[val] = i
        return False






                    
                    

    
