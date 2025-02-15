'''
2698. Find the Punishment Number of an Integer
Medium

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
 

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478

'''

# INTUITION :

'''
The solution involves iterating through each number i from 1 to n, calculating i * i, and checking if this square can meet the condition described above.

The intuition behind the implementation is that we can use recursion to check all possible substrings. For every position in the string representation of i * i, we recursively check all ways we could split the remaining string. If we reach the end of the string and the sum of the substrings equals i, then i * i is valid and should be included in our "punishment number" sum.

The check function in the code takes a string s, which represents the square of a number, an index i which indicates where to start partitioning, and an integer x that we are trying to match using the sum of substrings. It tries all possible ways to partition the string from index i onwards and returns true if any of those partitions sum up to x.

The main solution function punishmentNumber goes from 1 to n, checking each number i by calling the check function. If check returns true for a given i, it means we can sum up the substrings of i * i to get i, hence, we add i * i to our cumulative ans which is our punishment number.

This approach efficiently checks all possible partition points in the sequence and uses memorization by the nature of recursion to avoid rechecking the same combination of splits, leading to an optimal solution.

'''

class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if a square number can be split into two numbers that add up to the original number.
        def can_split_to_original(num_str: str, start_index: int, target_sum: int) -> bool:
            num_length = len(num_str)
            # If the starting index is beyond the string's length and target sum is zero, this is valid.
            if start_index >= num_length:
                return target_sum == 0
          
            current_num = 0
            # Consider different splits by incrementally including more digits.
            for j in range(start_index, num_length):
                current_num = current_num * 10 + int(num_str[j])
                # If the current number exceeds the target, there's no point in continuing.
                if current_num > target_sum:
                    break
                # Recursively check if the remaining string can fulfill the condition.
                if can_split_to_original(num_str, j + 1, target_sum - current_num):
                    return True
            return False

        # This variable holds the total sum of all square numbers fulfilling the condition.
        total_sum = 0
        # Iterate over the range 1 through n, inclusive.
        for i in range(1, n + 1):
            square_num = i * i  # Calculate the square of the number.
            # If the squared number can be split as desired, add to total sum.
            if can_split_to_original(str(square_num), 0, i):
                total_sum += square_num
      
        # Return the total sum of all such square numbers.
        return total_sum