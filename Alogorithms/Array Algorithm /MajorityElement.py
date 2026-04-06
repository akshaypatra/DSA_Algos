'''
Majority element  algorithm :

        TC : O(n)
        SC : O(1)

        We use the same idea of approach 1 above but actually, we don't have to use HashMap.
        We use two variables res and majority.

        ⭐️ Points

            - res is return value.
            - majority is frequency of majority number(= res).
            - Every time current number is the same as res, we add +1 to majority. If not, we add -1 to majority.
            - When majority is 0, it's time to change majority number(= res), because every time current number and res are different,
            we add -1 to majority, so if majority is 0, that means a current majority number(= res) is not the majority number anymore
            That's why when majority is 0, update res with current number.
'''

'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
def majorityelement(nums):
        
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res