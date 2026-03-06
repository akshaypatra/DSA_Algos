'''

1784. Check if Binary String Has at Most One Segment of Ones
Solved
Easy

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
'''

class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        if len(s)==1 :
            if s=='0':
                return False
            return True

        prev_one_index = 0
        for i in range(1,len(s)):
            if s[i]=="1" :
                if i-prev_one_index==1 :
                    prev_one_index =i
                else :
                    return False
        return True
            