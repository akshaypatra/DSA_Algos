'''
1513. Number of Substrings With Only 1s
Solved
Medium

Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.

'''

MOD = 10**9 + 7
class Solution:
    def numSub(self, s: str) -> int:


        def combination(n):
            return (n*(n+1))//2
        
        counter=[]
        c=0

        for i in s:
            if i=="1":
                c+=1
            else:
                counter.append(c)
                c=0
        
        if c>0:
            counter.append(c)

        res=0
        for j in counter:
            res+=combination(j)
        
        return res%MOD


