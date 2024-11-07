'''

2275. Largest Combination With Bitwise AND Greater Than Zero
Solved
Medium
Topics
Companies
Hint
The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

 

Example 1:

Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
Example 2:

Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
 

Constraints:

1 <= candidates.length <= 105
1 <= candidates[i] <= 107

'''

MAX_N_BITS = 24

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
         # Initialize an array to count bits for each of the 32 positions
        # bit_count = [0] * 32
        
        # # Count the number of '1's at each bit position across all candidates
        # for num in candidates:
        #     for i in range(32):  # Check each bit position (0 to 31)
        #         if num & (1 << i):  # If the ith bit is set
        #             bit_count[i] += 1
        
        # # The result is the maximum count in bit_count
        # return max(bit_count)



        # Solution 2

        max_set = 1 # Any one element is > 0
        mask = 1
        for shift in range(MAX_N_BITS):
            count = 0
            for num in candidates:
                if num & mask:
                    count += 1
            if max_set < count:
                max_set = count
            mask <<= 1
        return max_set
            
            
