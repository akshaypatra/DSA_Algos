'''

88. Merge Sorted Array
Solved
Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        

        # Approach : two pointer (starting from end)

        # edge case
        if n==0 : return

        # end_index for replacing zeroes
        len1=len(nums1)
        end_index = len1-1

        while n>0 and m>0 :

            if nums2[n-1]>=nums1[m-1] :
                '''
                if the nums2[n-1] is greater ,then directly replace the zero on end_index with the nums2 and decrement the end_index and n
                '''
                nums1[end_index]=nums2[n-1]
                n-=1
            else :
                '''
                if nums1[m-1] is greater ,then first put it on the end_index and decrement the end_index and m
                '''
                nums1[end_index]=nums1[m-1]
                m-=1
            end_index-=1

        '''
        fill the remaining zeroes with elements of nums2
        '''
        while n>0 :
            nums1[end_index]=nums2[n-1]
            n-=1
            end_index-=1



