'''

242. Valid Anagram
Solved
Easy

Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


'''

from collections import Counter,defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''

        Anagram :  a word or phrase made by transposing the letters of another word or phrase. 
                    The word "secure" is an anagram of "rescue."

        Intuition : usining hashset to count the characters in both strings and compare values

        '''

        '''

        # Brute force solution O(n) -> beats 76%
        if len(s)!=len(t):
            return False

        d1=defaultdict(int)
        d2=defaultdict(int)

        for i in s:
            d1[i]+=1
        
        for j in t:
            d2[j]+=1
        
        for i in d1.keys():
            if d1[i]!=d2[i]:
                return False
        
        return True

        '''



        #Using Counter  -> Beats 90%
        d1=Counter(s)
        d2=Counter(t)

        if len(s)!=len(t):
            return False

        for i in d1.keys():
            if d1[i]!=d2[i]:
                return False
        
        return True
            

        