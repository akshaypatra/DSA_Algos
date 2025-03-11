'''
1358. Number of Substrings Containing All Three Characters
Solved
Medium

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

'''

class Solution:
    def numberOfSubstrings(self, string: str) -> int:
        # count=0
        # for i in range(len(s)-1):
        #     for j in  range(i+1,len(s)):
        #         new_s=s[i:j+1]
        #         if ("a" in new_s) and ("b" in new_s) and ("c" in new_s):
        #             count+=1
        # return count


        
        last_seen_index = {"a": -1, "b": -1, "c": -1}
   
        answer = 0

        for index, char in enumerate(string):

            last_seen_index[char] = index

            answer += min(last_seen_index.values()) + 1
        return answer
