'''

3. Longest Substring Without Repeating Characters
Solved
Medium

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        '''

        Sliding Window algorithm

        -> Time complexity : O(n)

        '''

        i = 0
        j = 0
        max_len = 0
        visited = set()

        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1 
            else:
                visited.remove(s[i])
                i += 1  

        return max_len


            
            
        