'''

167. Two Sum II - Input Array Is Sorted
Solved
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        '''
        # BruteForce approach :20 / 24 testcases passed
        '''

        # for i in range(len(numbers)):
        #     remaining=target-numbers[i]
        #     for j in range(i+1,len(numbers)):
        #         if numbers[j]==remaining:
        #             return [i+1,j+1]
        
       
    #-------------------------------------------------------------

        '''

        # Approach two : binary search
        -> Accepted 24 / 24 testcases passed
        -> not optimised

        '''

        # def binary_search(arr,target,l,h):
        #     if l > h:
        #         return -1  

        #     mid = l + (h - l) // 2  

        #     if arr[mid] == target:
        #         return mid
        #     elif target > arr[mid]:
        #         return binary_search(arr, target, mid + 1, h) 
        #     else:
        #         return binary_search(arr, target, l, mid - 1) 
        
        # for i in range(len(numbers)):
        #     remaining=target-numbers[i]
        #     if remaining in numbers[i+1:]:
        #         return [i+1,binary_search(numbers,remaining,i+1,len(numbers)-1)+1]

     #-------------------------------------------------------------

        '''
        Approach 3 : two pointers
        -> O(n) time complexity

        '''

        p1=0
        p2=len(numbers)-1

        while p2>p1:
            if numbers[p2]+numbers[p1]==target :
                return [p1+1,p2+1]
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1
    



