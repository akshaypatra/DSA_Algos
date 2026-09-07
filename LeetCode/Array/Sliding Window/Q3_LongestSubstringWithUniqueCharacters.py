'''
leetcode 3 Longest Subtring without repeating characters

Given a string s, find the length of the longest 
substring without repeating characters.

 
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
'''

# Topics : array,sliding window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Using sliding window

        # i=0
        # j=0
        # max_len=0
        # visited=[]
        # while j<len(s):
            
        #     if s[j] not in visited:
        #         visited.append(s[j])
        #         j+=1
        #     else:
        #         visited=[]
        #         i+=1
        #         j=i
        #     if (j-i)>max_len:
        #         max_len=j-i
        # return max_len


        # Optimisation (j is not reinitialised)

        i=0
        j=0
        max_len=0
        visited=set()
        while j<len(s):
            
            if s[j] not in visited:
                visited.add(s[j])
                j+=1
                cur_max=j-i
            else:
                visited.remove(s[i])
                i+=1
                cur_max-1
                
            max_len=max(max_len,cur_max)
        return max_len