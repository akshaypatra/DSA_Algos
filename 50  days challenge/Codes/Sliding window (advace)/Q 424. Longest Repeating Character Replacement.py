'''

424. Longest Repeating Character Replacement
Solved
Medium

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}  # To keep track of character frequencies in the window
        max_freq = 0  # Most frequent character count in the window
        p1 = 0  # Left pointer
        max_length = 0

        for p2 in range(len(s)):  
            freq[s[p2]] = freq.get(s[p2], 0) + 1
            max_freq = max(max_freq, freq[s[p2]])

            # If window size minus most frequent char count > k, shrink window
            while (p2 - p1 + 1) - max_freq > k:
                freq[s[p1]] -= 1
                p1 += 1  # Shrink the window

            max_length = max(max_length, p2 - p1 + 1)

        return max_length
                
                
