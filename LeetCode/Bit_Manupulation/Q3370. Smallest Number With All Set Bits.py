'''
3370. Smallest Number With All Set Bits
Solved
Easy

You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".

 

Constraints:

1 <= n <= 1000
'''

# Solution 1 

class Solution:
    def smallestNumber(self, n: int) -> int:
        b=bin(n)[2:]
        i='1'*len(b)

        return int(i,2)


# Solution 2 

class Solution:
    def smallestNumber(self, n: int) -> int:
        outputs = {
            1: 1,
            2: 3,
            4: 7,
            8: 15,
            16: 31,
            32: 63,
            64: 127,
            128: 255,
            256: 511,
            512: 1023,
            1024: 2047,
        }
        prev = 1
        for output in outputs.keys():
            if output > n:
                return outputs[prev]
            prev = output
        
        return outputs[1024]
