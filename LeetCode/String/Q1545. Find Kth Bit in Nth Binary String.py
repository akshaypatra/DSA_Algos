'''

1545. Find Kth Bit in Nth Binary String

Medium

Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
 

Constraints:

1 <= n <= 20
1 <= k <= 2n - 1

'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findKthBitHelper(n, k):
            # Base case: when n == 1, the string is just "0"
            if n == 1:
                return '0'
            
            # Calculate the length of S_n
            length = (1 << n) - 1  # Length of S_n is 2^n - 1
            
            # Middle element position
            mid = length // 2 + 1
            
            if k == mid:
                return '1'  # The middle element is always '1'
            elif k < mid:
                return findKthBitHelper(n - 1, k)  # Check in the left part
            else:
                # k is in the right part, map it to the left part's index
                mirrored_index = length - k + 1
                return '1' if findKthBitHelper(n - 1, mirrored_index) == '0' else '0'

        return findKthBitHelper(n, k)