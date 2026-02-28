'''
1680. Concatenation of Consecutive Binary Numbers
Solved
Medium

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 105

'''

MOD = 10**9 + 7
ans = [0]*(10**5 + 1)
res = 0
length = -1
for i in range(1, 18):
    for e in range(2**(i - 1), min(2**i, len(ans))):
        res = ((res << i) | e) % MOD
        ans[e] = res

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return ans[n]