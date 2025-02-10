'''
3174. Clear Digits
Solved
Easy

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".

 

Constraints:

1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.

'''

class Solution:
    def clearDigits(self, s: str) -> str:

        '''
        -> beats 100%
        -> time complexity : O(n)

        '''

        stack=[]
        p1=0
        while p1<len(s):
            if s[p1] not in '1234567890':
                stack.append(s[p1])
            else:
                if stack:
                    stack.pop()
            p1+=1

        return ''.join(stack)
            

