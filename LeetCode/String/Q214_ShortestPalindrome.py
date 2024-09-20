'''
Leetcode 214 : Shortest Palindrome

You are given a string s. You can convert s to a 
palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 
Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.

'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        # BruteForce Solution : find the longest palindrome and copy the remaining string and adding (the reverse ) it to start.

        def is_palindrome(s,l,r):
            while l <=r:
                if s[l]!=s[r]:
                    return False
                l,r=l+1,r-1
            return True
        
        for r in reversed(range(len(s))):
            if is_palindrome(s,0,r):
                suffix=s[r+1:]
                return suffix[::-1]+s
        return ""

        '''

        # Rabin karp method :

        prefix=0
        suffix=0

        base=29
        last_index=0
        power=1
        mod=10**9 + 7

        for i,c in enumerate(s):
            char=(ord(c)-ord('a')+1)

            prefix=(prefix*base)%mod
            prefix=(prefix+char)%mod
            suffix=(suffix+char*power)%mod
            power=(power*base)%mod

            if prefix ==suffix:
                last_index=i




        suffix=s[last_index+1:]
        return suffix[::-1] + s
        
