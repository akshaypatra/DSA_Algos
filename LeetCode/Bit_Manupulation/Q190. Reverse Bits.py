'''
190. Reverse Bits
Solved
Easy

Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 

Constraints:

0 <= n <= 231 - 2
n is even.'''


class Solution:
    def reverseBits(self, n: int) -> int:
        # binary_32 = format(n & 0xFFFFFFFF, '032b')
        # return int(str(binary_32)[::-1],2)

        
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n = n >> 1
        return result
