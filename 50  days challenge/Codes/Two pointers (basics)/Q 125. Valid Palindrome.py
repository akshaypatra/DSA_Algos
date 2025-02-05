'''

125. Valid Palindrome
Solved
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''

        Using Two pointers

        Intuition : 
        -> converting each string to  sequence of alphnumeric characters
        -> performing lowercase operation
        -> creating a new string using concatenation 
        -> using two pointer to compare from start and end

        -> time complexity : O(n)

        '''



        new_str=""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz1234567890":
                new_str+=i
        

        p1=0
        p2=len(new_str)-1
        
        while p2>p1:
            if new_str[p1]==new_str[p2]:
                p1+=1
                p2-=1
            else:
                return False
        return True



        '''
        Optimised Code using isalnum function and string slicing
        '''

        # a=''.join([i for i in s if i.isalnum()])

        # m=a.lower()

        # b = m[::-1]

        # if b == m :
        #     return True
        # else :
        #     return False