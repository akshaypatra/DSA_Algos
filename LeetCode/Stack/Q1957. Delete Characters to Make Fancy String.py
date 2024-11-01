'''

1957. Delete Characters to Make Fancy String

Easy

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.

'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]

        l=len(s)
        i=1

        stack.append(s[0])
        prev_str=s[0]
        count=1

        while i<l:
            
            if s[i]==prev_str:
                count+=1
            else:
                count=1
                prev_str=s[i]
            
            if count<3:
                stack.append(s[i])
                i+=1
            else:
                i+=1
        return ''.join(stack)
