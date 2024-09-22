'''


Leetcode 440 : Kth smallest in lexicographical order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

'''

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1  

        while k > 0:
            steps = 0
            first = current
            last = current + 1

            while first <= n:
                steps += min(n + 1, last) - first  
                first *= 10
                last *= 10
            
            if steps <= k:  
                current += 1
                k -= steps
            else:  
                current *= 10
                k -= 1

        return current