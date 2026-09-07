'''
229. Majority Element II

Medium

Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        '''
        Approach 1 : Using Counter

        TC : O(n)
        SC : O(logn)
        '''
        # c = Counter(nums)

        # res=[]
        # for i in c.keys():
        #     if c[i]>len(nums)//3:
        #         res.append(i)
        
        # return res

        '''
        Approach 2 : Boyer Moore Extended - Majority element algorithm

        TC : O(n)
        SC : O(1)
        '''

        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verification step
        result = []

        if nums.count(cand1) > len(nums) // 3:
            result.append(cand1)

        if cand2 != cand1 and nums.count(cand2) > len(nums) // 3:
            result.append(cand2)

        return result

