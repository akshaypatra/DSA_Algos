'''
670. Maximum Swap

Medium

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters (digits)
        num_list = list(str(num))
        
        # Create a list to store the index of the maximum digit from the current position to the end
        max_idx = [-1] * len(num_list)
        max_idx[-1] = len(num_list) - 1
        
        # Traverse from right to left to find the maximum digit index at each position
        for i in range(len(num_list) - 2, -1, -1):
            if num_list[i] > num_list[max_idx[i + 1]]:
                max_idx[i] = i
            else:
                max_idx[i] = max_idx[i + 1]
        
        # Now find the first place where a swap would result in a bigger number
        for i in range(len(num_list)):
            if num_list[i] < num_list[max_idx[i]]:
                # Swap the digits
                num_list[i], num_list[max_idx[i]] = num_list[max_idx[i]], num_list[i]
                break
        
        # Convert the list back to an integer and return the result
        return int("".join(num_list))
