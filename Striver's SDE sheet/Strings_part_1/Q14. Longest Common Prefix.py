'''
14. Longest Common Prefix
Solved
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Approach 1 : Sorting on based on alphabets

        Traverse the starting and ending string and check how much common is there

        TC : O(nlogn)
        SC : O(1)
        '''

        strs.sort()

        s=""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i]==strs[-1][i]:
                s+=strs[0][i]
            else :
                break
        return s

        '''
        Approach 1 : Vertical scanning

        This solution is the vertical scanning approach that is discussed in the official solution, slightly modified for Python. The idea is to scan the the first character of every word, then the second character, etc. until a mismatch is found. At that point, we return a slice of the string which is the longest common prefix.

        This is superior to horizontal scanning because even if a very short word is included in the array, the algorithm won't do any extra work scanning the longer words and will still end when the end of the shortest word is reached.

        TC : O(n*m)
        SC : O(1)
        '''

        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base