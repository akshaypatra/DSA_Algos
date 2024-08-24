# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

# The closest is defined as the absolute difference minimized between two integers.

# Example 1:

# Input: n = "123"
# Output: "121"
# Example 2:

# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

# Constraints:

# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 1018 - 1].


# Solution 
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        
        candidates = set()
        
        #  palindromic numbers like 999...999 or 100...001
        candidates.add(str(10**(length - 1) - 1))  # for 999...999
        candidates.add(str(10**length + 1))  # for 100...001
        
        # Middle part for the palindrome, can be the original or +1, -1
        prefix = int(n[:(length + 1)//2])
        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                candidates.add(p + p[::-1])
            else:
                candidates.add(p + p[-2::-1])
        
        # Removing the original number n itself from the candidates (as it is stated in the problem itself)
        candidates.discard(n)
        
        # Finding the closest palindrome
        closest = None
        min_diff = float('inf')
        
        for candidate in candidates:
            diff = abs(int(candidate) - int(n))
            if diff < min_diff or (diff == min_diff and int(candidate) < int(closest)):
                min_diff = diff
                closest = candidate
        
        return closest