'''
1780. Check if Number is a Sum of Powers of Three
Solved
Medium
Topics
Companies
Hint
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        '''
        Hint : The number can not be represented as a sum of powers of 3 
            if it's ternary presentation  has a 2 in it (because 2 cannot be represented 
            using any power of 3)

        Intuition :  taking modulus of number , if remainder comes out to be 2 , then return false
        
        Beats 100%
        '''
        while n:
            s=n%3
            if s==2:
                return False
            else:
                n=n//3
        return True