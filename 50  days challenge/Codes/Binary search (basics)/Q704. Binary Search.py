'''
704. Binary Search
Solved
Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Solution 1 : Without recursion

        # l=0
        # h=len(nums)-1

        # while l<=h:
        #     mid=l+ (h - l) // 2

        #     if nums[mid]==target:
        #         return mid
            
        #     if target>nums[mid]:
        #         l=mid+1
        #     else:
        #         h=mid-1
        
        # return -1


        # Solution 2 : RECURSIVE 

        def binarySearch(l,h,target):
            if l<=h:
                mid=l+ (h-l)//2

                if nums[mid]==target:
                    return mid
                
                if target > nums[mid]:
                    return binarySearch(mid+1,h,target)
                else:
                    return binarySearch(l,mid-1,target)
            return -1
        
        return binarySearch(0,len(nums)-1,target)
            