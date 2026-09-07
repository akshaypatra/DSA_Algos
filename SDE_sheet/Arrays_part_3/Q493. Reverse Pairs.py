'''
493. Reverse Pairs
Solved
Hard

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

Constraints:

1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
'''

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        Approach 1 : Bruteforce - traversing and comparison from end
        (TLE - expected )

        TC : O(N^2)
        SC : O(1)

        '''

        # j = len(nums)-1
        # pairs = 0
        # while j > 0 :
        #     for i in range(j):
        #         if nums[i] > 2*nums[j]:
        #             pairs+=1

        #     j-=1
        # return pairs

        '''
        Approach 2 : Merge sort

        Steps :
        
        1. Recursively split the array into two halves : left half and right half
        2. Solve the problem for left and right independetly.
        3. Count reverse pairs between the sorted left and right halves , then merge them .

        4 6 8    1 2 3
        i          j

        Since both halves are sorted : if nums[i] > 2*nums[j] , then everything after i also works .

        we add (mid-i+1) to the count 

                [1,3,2,3,1]
                /         \
            [1,3,2]      [3,1]
            /    \        /   \
        [1,3]    [2]    [3]    [1]


        Time  = O(n log n)
        Space = O(n)
        '''

        def countPairs(left, mid, right):
            '''
            - We maintain a pointer j in right half . For each i in the left half we push j forward.

            '''
            count = 0
            j = mid + 1

            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - (mid + 1)

            return count

        def merge(left, mid, right):
            temp = []

            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1

            nums[left:right + 1] = temp

        def mergeSort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2

            count = mergeSort(left, mid)
            count += mergeSort(mid + 1, right)

            count += countPairs(left, mid, right)

            merge(left, mid, right)

            return count

        return mergeSort(0, len(nums) - 1)





        