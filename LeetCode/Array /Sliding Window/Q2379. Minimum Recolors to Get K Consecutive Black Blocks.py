'''

2379. Minimum Recolors to Get K Consecutive Black Blocks
Solved
Easy

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n

'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        count_W = 0  # Count of 'W' in the current window
        
        # Count 'W's in the first window of size k
        for j in range(k):
            if blocks[j] == 'W':
                count_W += 1
        
        min_count_W = count_W  # Set the initial minimum 'W' count
        
        # Slide the window across the string
        for j in range(k, len(blocks)):
            if blocks[j] == 'W':  # Include new character
                count_W += 1
            if blocks[i] == 'W':  # Exclude old character
                count_W -= 1
            i += 1  # Move left pointer
            
            min_count_W = min(min_count_W, count_W)  # Track the minimum
        
        return min_count_W
                
            
            

            