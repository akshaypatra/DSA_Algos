'''
2566. Maximum Difference by Remapping a Digit
Solved
Easy

You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 108

'''
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
      
        # Replace the first digit of the string with '0' to create the minimum number
        # This works under the assumption that the first digit is not '0'
        # Otherwise, 'mi' would become a different number of digits.
        min_num = int(num_str.replace(num_str[0], '0'))
      
        # Iterate over the digits of the string
        for digit in num_str:
            # If a digit is not '9', we can create the max number
            # by replacing the first occurrence of that digit with '9'
            if digit != '9':
                max_num = int(num_str.replace(digit, '9'))
                # Return the difference between the max number and the min number
                return max_num - min_num
              
        # If all digits are '9', return the difference between the original number and min_num
        return num - min_num

