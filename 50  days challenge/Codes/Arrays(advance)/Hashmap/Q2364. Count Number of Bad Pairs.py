'''

2364. Count Number of Bad Pairs
Solved
Medium

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

'''

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        '''
        -> counter good pairs and subtracted it from total pairs
        ->  (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j)
        ->  counter of nums[i] - i. To be efficient, use a HashMap.

        -> O(n) - time complexity


        '''
        # hashmap=defaultdict(list)
        # l=len(nums)

        # for i in range(l):
        #     res=nums[i]-i
        #     hashmap[res].append(i)
        

        # total_pairs=(l*(l-1))//2

        # good_pairs=0
        # for i in hashmap.keys():
        #     l1=len(hashmap[i])
        #     if l1 >=2 :
        #         good_pairs+=(l1*(l1-1))//2
        
        # return total_pairs - good_pairs



        '''

        Optimised Code using Counter

        '''

        count = 0 
        length = len(nums)
        nums_new = [ num - index for index, num in enumerate(nums)]

        count = Counter(nums_new)
      
        total_pairs = length*(length-1)/2 

        for key, val in count.items(): 

            if val!=1: 
                #print ('val', val)
                total_pairs -= val*(val-1)/2

        return int(total_pairs)



        
