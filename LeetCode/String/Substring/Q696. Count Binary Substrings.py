'''
696. Count Binary Substrings
Solved
Easy


Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        00110011 -> 2 0's , 2 1's ,2 O's,2 1's -> [2,2,2,2] -> min(2,2)+min(2,2)+min(2,2) + min(2,2) = 6

        10101 -> [1,1,1,1,1] -> min(1,1)+min(1,1)+min(1,1) + min(1,1)

        '''

        l=[]
        prev=s[0]
        count=1

        if len(s)==1:
            return 0
        
        for i in range(1,len(s)):
            if s[i]!=prev:
                prev=s[i]
                l.append(count)
                count=1
            else:
                count+=1
        l.append(count)
        
        i=1
        res=0
        while i<len(l):
            res+=min(l[i-1],l[i])
            i+=1
        return res


