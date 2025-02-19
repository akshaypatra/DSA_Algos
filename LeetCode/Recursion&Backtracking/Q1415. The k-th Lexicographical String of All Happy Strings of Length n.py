'''

1415. The k-th Lexicographical String of All Happy Strings of Length n
Solved
Medium

A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100

'''
class Solution:
    def getHappyString(self, length: int, index: int) -> str:
        # Helper function for depth-first search to find all happy strings
        def dfs(current_str):
            # Base condition: if current string reaches the desired length, add to results
            if len(current_str) == length:
                happy_strings.append(current_str)
                return
            # Iterate through all possible characters
            for char in 'abc':
                # Avoid repeating characters
                if current_str and current_str[-1] == char:
                    continue
                # Recursively build the string
                dfs(current_str + char)

        # List to store all possible happy strings
        happy_strings = []
        # Start the DFS with an empty string
        dfs('')
        # If there are fewer than k happy strings, return an empty string
        # Otherwise, return the k-th happy string (1-indexed)
        return '' if len(happy_strings) < index else happy_strings[index - 1]