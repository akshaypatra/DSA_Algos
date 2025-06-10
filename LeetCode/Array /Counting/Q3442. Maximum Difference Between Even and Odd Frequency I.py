'''
3442. Maximum Difference Between Even and Odd Frequency I
Solved
Easy

You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.

'''

class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)


        a1=0
        a2=float("inf")

        for i in c.keys():
            if c[i]%2!=0 and c[i]>a1:
                a1=c[i]
            if c[i]%2==0 and  c[i]<a2:
                a2=c[i]
        return a1-a2