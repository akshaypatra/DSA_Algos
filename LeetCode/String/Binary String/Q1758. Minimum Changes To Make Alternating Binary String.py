'''
1758. Minimum Changes To Make Alternating Binary String
Solved
Easy

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
'''

class Solution:
    def minOperations(self, s: str) -> int:
        
        '''
        Approach 1 : comparison and Miss counter 

        for every alternating string there are two combination :
            1. starting with 1
            2. starting with zero

        example 0100 -> 
            - option 1 : 1010 -> total miss (after comparison) : 3
            - option 2 : 0101 -> total miss : 1

            - return the minimum miss 
        '''

        # def alt(bit):
        #     if bit=="0":
        #         return "1"
        #     else :
        #         return "0"


        # if len(s)==1 :
        #     return 0

        # count_0=0
        # count_1=0

        # start_0="0"
        # start_1="1"

        # for i in s :
        #     if start_0!=i:
        #         count_0 +=1

        #     if start_1!=i:
        #         count_1 +=1

        #     start_0=alt(start_0)
        #     start_1=alt(start_1)
        
        # return min(count_0,count_1)


        '''
        Approach 2 
        '''
        start0 = 0
        start1 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        
        return min(start0, start1)

        
        