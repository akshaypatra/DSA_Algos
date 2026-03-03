'''
1545. Find Kth Bit in Nth Binary String
Solved
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
        ''' 
        Bruteforce approach 
        '''

        # prev='0'

        # if n==1:
        #     return prev

        # for _ in range(1,n):
        #     cur_str=prev+"1"
        #     for c in prev[::-1]:
        #         cur_str+="1" if c=="0" else "0"
        #     prev=cur_str
        
        # return prev[k-1]


        '''
        Optimized approach 

        using XOR operation to reduce the time Complexity from O(n^2) to O(n)

        s="1011"
        temp = int(s,2)
        inverted_bit = temp ^ (2**(len(s)-1))
        res=bin(inverted_bit)[2:]

        '''

        # prev='0'

        # if n==1:
        #     return prev

        # for _ in range(1,n):
        #     # adding "1"
        #     cur_str=prev+"1"

        #     # String inversion
        #     temp = int(prev,2)
        #     inverted_bit = temp ^ (2**(len(prev))-1)
        #     res=bin(inverted_bit)[2:]

        #     prev=cur_str+res[::-1]
        
        # return prev[k-1]



        '''
        Recursive approach 
        '''

        # Base case: for S1, return '0'
        if n == 1:
            return "0"

        # Calculate the length of Sn
        length = 1 << n  # Equivalent to 2^n

        # If k is in the first half of the string, recurse with n-1
        if k < length // 2:
            return self.findKthBit(n - 1, k)

        # If k is exactly in the middle, return '1'
        elif k == length // 2:
            return "1"

        # If k is in the second half of the string
        else:
            # Find the corresponding bit in the first half and invert it
            corresponding_bit = self.findKthBit(n - 1, length - k)
            return "1" if corresponding_bit == "0" else "0"




            




        

