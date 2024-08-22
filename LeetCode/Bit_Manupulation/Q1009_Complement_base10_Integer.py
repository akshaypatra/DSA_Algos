# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        

        if n == 0 :
            return 1
        
        # calculates the number of bits for the number
        bits = n.bit_length()    

        # shift the 1 to the left bits times ((1 << bits) - 1) return a integer after shifting the bits)
        shift = (1 << bits) - 1 #subtracting 1 to reduce the size of binary number 

        return n^shift  #return integer after performing xor operation on n and shift 
     
# Note : xor returns 1 for diffrent bits and 0 when bits are same (helps to find complement) 