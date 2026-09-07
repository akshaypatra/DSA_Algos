'''
3090. Maximum Length Substring With Two Occurrences
Solved
Easy

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''
            - at most 2 same characters.
            - maximum length possible
            - use hashmap to count characters
            - two pointers approach

            b c b b b c b a
            0 1 2 3 4 5 6 7
        '''

        count = defaultdict(int)
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            count[ch] += 1

            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
                
                


            
