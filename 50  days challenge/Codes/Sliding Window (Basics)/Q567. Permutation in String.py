'''

567. Permutation in String
Solved
Medium

Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])  # Initial window
        
        if s1_count == s2_count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2_count[s2[r]] += 1  # Add new character to window
            s2_count[s2[l]] -= 1  # Remove left character from window
            
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]  # Remove zero-count characters
            
            l += 1  # Sliding window forward
            
            if s1_count == s2_count:
                return True

        return False


    