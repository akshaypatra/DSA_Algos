'''
1855. Maximum Distance Between a Pair of Values
Solved
Medium

You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

 

Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 105
Both nums1 and nums2 are non-increasing.
'''
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        '''
        Approach 1 : bruteforce  (TL exceeded)

        TC : O(n^2)
        SC : O(1)
        '''

        # p1=0
        # p2=0
        # max_distance = 0

        # for i in range(len(nums1)):
        #     if i<len(nums2):
        #         for j in range(i,len(nums2)) :
        #             if nums1[i]<=nums2[j]:
        #                 max_distance = max(j-i,max_distance)
        #             else :
        #                break
        
        # return max_distance


        '''
        Approach 2 : Optimization 

        -> Reduce O(n^2) to O(n)
        -> Explaination

        Let i be the index pointer in array nums1 (A), and j be the index pointer in array nums2 (B).

        Since both arrays are non-increasing:

        Advancing i and j can only keep or decrease A[i], andB[j] respectively.
        We want to maximize:

        j−i

        Thus, our goal is:

            keep i as far left as possible,
            move j as far right as possible.
        

        Algorithm :
        
        The pointers are initialized at i=0 and j=1. For each position j in B, the algorithm identifies the smallest feasible index i
        in A.

            - If A[i]≤B[j], the current index i is valid.
                - The pointer i remains stationary to maximize the potential distance j−i.

            - If A[i]>B[j], the index i is no longer feasible.
                - Since B[j] will not increase for larger values of j, this specific i cannot satisfy the constraint for any future
                iterations.
                - Consequently, i must advance.

        The pointer j increments in every iteration as array B is processed in a single left-to-right pass.


​       Because j increases in every iteration while i increases only when the validity constraint is violated:

            - If no valid pairs exist where i<j, i and j will increment at the same rate.
            - The final result is calculated as:
                    j−i−1
            ​
            - This calculation returns the maximum valid distance found during the traversal, or 0 if the pointers incremented together
              throughout the process.

        '''


        i, j = 0, 1

        while i < len(nums1) and j < len(nums2):
            i += nums1[i] > nums2[j]
            j += 1

        return j - i - 1