'''

1922. Count Good Numbers
Solved
Medium

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
 

Constraints:

1 <= n <= 1015

'''

class Solution:
    def countGoodNumbers(self, n: int) -> int:
    
        MODULO = 10**9 + 7 
      
        # Define the power function to calculate (x^n) % MODULO using binary exponentiation.
        def my_pow(base, exponent):
            result = 1
            while exponent > 0:
                # If exponent is odd, multiply the result with base.
                if exponent % 2 == 1:
                    result = (result * base) % MODULO
                # Square the base and reduce the exponent by half.
                base = (base * base) % MODULO
                exponent //= 2
            return result
      
        # Number of primes at odd positions is 5 (2,3,5,7). Hence, we use 5 as the base.
        # Number of evens at even positions is 4 (0,2,4,6,8). Hence, we use 4 as the base. Even positions are considered 0-indexed here.
        # The +1 is needed when n is odd, to calculate 5 raised to the (n//2 + 1).
        return (my_pow(5, (n + 1) // 2) * my_pow(4, n // 2)) % MODULO
