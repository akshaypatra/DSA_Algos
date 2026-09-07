'''
5. Longest Palindromic Substring
Solved
Medium

Given a string s, return the longest palindromic substring in s.
 
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        '''
        Approach 1 : check all substring

        TC : O(n^3)
        '''

        # def isPalindrome(i,j):
        #     p1=i
        #     p2=j-1

        #     while p1<p2 :
        #         if s[p1] != s[p2]:
        #             return False
        #         p1+=1
        #         p2-=1
            
        #     return True
        
        # for length in range(len(s),0,-1):
        #     for start in range(len(s)-length+1):
        #         if isPalindrome(start,start+length):
        #             return s[start : start+length]
        # return ""



        '''
        Approach 2 : Dynamic programming

        - We know that all substrings of length 1 are palindromes. From this, we can check if each substring of length 3 is a palindrome
        using the above fact. We just need to check every i, j pair where j - i = 2. Once we know all palindromes of length 3, we can 
        use that information to find all palindromes of length 5, and then 7, and so on.

        - What about even-length palindromes? A substring of length 2 is a palindrome if both characters are equal. That is, i, i + 1
        is a palindrome if s[i] == s[i + 1]. From this, we can use the earlier logic to find all palindromes of length 4, then 6, and
        so on.

        - Let's use a table dp with dimensions of n * n. dp[i][j] is a boolean representing if the substring with inclusive bounds i, j
        is a palindrome. We initialize dp[i][i] = true for the substrings of length 1, and then dp[i][i + 1] = (s[i] == s[i + 1]) for
        the substrings of length 2.

        - Now, we need to populate the table. We iterate over all i, j pairs, starting with pairs that have a difference of 2
        (representing substrings of length 3), then pairs with a difference of 3, then 4, and so on. For each i, j pair, we check the
        condition from earlier:

        s[i] == s[j] && dp[i + 1][j - 1]

        - If this condition is true, then the substring with inclusive bounds i, j must be a palindrome. We set dp[i][j] = true.

        Algorithm

        1. Initialize n = s.length and a boolean table dp with size n * n, and all values to false.

        2. Initialize ans = [0, 0]. This will hold the inclusive bounds of the answer.

        3. Set all dp[i][i] = true.

        4. Iterate over all pairs i, i + 1. For each one, if s[i] == s[i + 1], then set dp[i][i + 1] = true and update ans = [i, i + 1].

        5. Now, we populate the dp table. Iterate over diff from 2 until n. This variable represents the difference j - i.

        6. In a nested for loop, iterate over i from 0 until n - diff.

                - Set j = i + diff.
                - Check the condition: if s[i] == s[j] && dp[i + 1][j - 1], we found a palindrome.
                - In that case, set dp[i][j] = true and ans = [i, j]
                
        7. Retrieve the answer bounds from ans as i, j. Return the substring of s starting at index i and ending with index j.


        '''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]


