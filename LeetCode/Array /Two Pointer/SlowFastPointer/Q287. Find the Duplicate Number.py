'''
287. Find the Duplicate Number
Solved
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        '''
        Approach 1 : sort and check for consecutive

        not appropriate answer as nums is modified

        TC : O(n)
        SC : O(1)

        '''
        # nums.sort()
        
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return nums[i]


        '''
        Approach 2 :  Two pointers - Slow pointer Fast pointer  (Floyd's cycle finsing algorithm)

        Phase 1: Use slow and fast pointers. fast moves twice as fast. They are guaranteed to meet inside the cycle.
        Phase 2: Reset slow to the start (0) and keep fast at the meeting point. Move both one step at a time.
                Since fast is already inside the loop, the mathematical distance from "start to cycle entry" equals "meeting point 
                to  cycle entry." They will collide exactly at the duplicate number (the cycle entrance).

        1. Initialize: Start slow and fast at index 0.
        2. Find Intersection:
            - Move slow to nums[slow].
            - Move fast to nums[nums[fast]].
            - Repeat until slow == fast.
        3. Find Entrance:
            - Reset slow to 0.
            - Move both pointers one step at a time (slow = nums[slow], fast = nums[fast]) until they meet.
        4. Return: The value where they meet is the duplicat

     
        '''

        slow = 0
        fast = 0

        while True :

            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast :
                break
        
        slow=0
        while slow!=fast :
            slow = nums[slow]
            fast = nums[fast]

        return slow







        

        
        