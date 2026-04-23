'''
2615. Sum of Distances
Solved
Medium

You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

 

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109


'''

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        '''

        Approach 1 : Hashmap (Time limit exceeded)

        nums = [1,3,1,1,2]

        d = {
            1 : 0,2,3
            3 : 1
            2 : 1
        }

        '''
        # d = defaultdict(list)

        # for i in range(len(nums)):
        #     d[nums[i]].append(i)
        

        # res=[0 for _ in range(len(nums))]
        # for k in d.keys() :
        #     if len(d[k])==1:
        #         continue
        #     for i in d[k] :
        #         for j in range(len(d[k])):
        #             if i==d[k][j] :
        #                 continue
                    
        #             res[i]+=abs(d[k][j]-i)
        # return res


        '''
        Approach 2 : Grouping + prefix sum

        '''

        n = len(nums)
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        res = [0] * n
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx
        return res

