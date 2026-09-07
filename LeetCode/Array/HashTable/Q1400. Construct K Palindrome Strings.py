'''

1400. Construct K Palindrome Strings

Medium

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105

'''

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        '''

        # Bruteforce solution using hints and hashmap

        if len(s)<k:
            return False
        

        d={}
        for c in s:
            if c not in d.keys():
                d[c]=1
            else:
                d[c]+=1
        

        count_odd=0
        for i in d.keys():
            if d[i]%2!=0:
                count_odd+=1
        
        if count_odd <= k:
            return True
        else:
            return False

        '''

        # optimised solution (same logic , only using counter to count number of characters)

        if k>len(s):
            return False
        
        count = Counter(s)
        odd=0
        for cnt in count.values():
            odd+=cnt%2
        return odd <= k
