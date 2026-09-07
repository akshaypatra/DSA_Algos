'''
Leetcode : 1945 Sum of digits after convert
You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.

 

Example 1:

Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.
Example 2:

Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.
'''


# Solution
class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def sum_of_digits(n):
            # s=str(n)
            # sum_=0
            # for i in s:
            #     sum_ +=int(i)
            # return sum_

            return sum(int(digit) for digit in str(n))
        
        d={
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
        'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
        'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
        'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
        }

        # logical error in while loop (concatenation should be done before sum)
        # sum_=0
        # n=1
        # for i in s:
        #     sum_+=d[i]
        
        # if k==1:
        #     return sum_
        
        # while  n<k+1:
        #     sum_=sum_of_digits(sum_)
        #     n+=1


        # fixed code
        sum_ = 0
        num_str = ''.join(str(d[char]) for char in s)

        sum_ = sum_of_digits(int(num_str))
        
        # Apply the transformation `k-1` times
        for _ in range(k-1):
            sum_ = sum_of_digits(sum_)


        return sum_ 



        
        
