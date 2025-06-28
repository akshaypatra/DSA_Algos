'''
2099. Find Subsequence of Length K With the Largest Sum
Solved
Easy

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
'''

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        '''
        Hashmap and Proirity Queue 

        val -> elements
        priority -> index
        '''

        '''
        hashset=[]
        for i in range(len(nums)):
            hashset.append((nums[i],i))
        hashset.sort()
        subseq=hashset[len(hashset)-k:]


        pq=[]
        for i,j in subseq:
            heapq.heappush(pq,(j,i))


        res=[]
        while pq:
            i,j=heapq.heappop(pq)
            res.append(j)
        return res
        '''


        #  Optimised Solution using lambda function

   
        indexed_nums = [(num, i) for i, num in enumerate(nums)]

        # Sort by value and take the k largest elements
        top_k = sorted(indexed_nums, key=lambda x: x[0])[-k:]

        # Sort the top k elements by original index
        top_k.sort(key=lambda x: x[1])

        return [num for num, _ in top_k]



        


            
            





        