'''
567. Permutation in String
Medium
Topics
Companies
Hint
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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, it can't be a substring
        if len(s1) > len(s2):
            return False
        
        # Initialize frequency arrays for s1 and the first window of s2
        s1_count = [0] * 26  # Frequency array for s1
        s2_count = [0] * 26  # Frequency array for the window in s2
        
        # Populate the frequency array for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # Check if the first window is a valid permutation
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            if matches == 26:  # If all counts match, return True
                return True
            
            # Slide the window: remove the character going out of the window
            left_index = ord(s2[i - len(s1)]) - ord('a')
            s2_count[left_index] -= 1
            if s2_count[left_index] == s1_count[left_index]:
                matches += 1
            elif s2_count[left_index] + 1 == s1_count[left_index]:
                matches -= 1
            
            # Add the character coming into the window
            right_index = ord(s2[i]) - ord('a')
            s2_count[right_index] += 1
            if s2_count[right_index] == s1_count[right_index]:
                matches += 1
            elif s2_count[right_index] - 1 == s1_count[right_index]:
                matches -= 1
        
        # Final check after the last window
        return matches == 26
