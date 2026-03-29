'''
2839. Check if Strings Can be Made Equal With Operations I
Solved
Easy

You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

Example 1:

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
Example 2:

Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: It is not possible to make the two strings equal.
 

Constraints:

s1.length == s2.length == 4
s1 and s2 consist only of lowercase English letters.
'''
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        '''
        Intuition
        We are allowed to swap characters only when the index difference is 2.

        This means:

        index 0 ↔ 2
        index 1 ↔ 3

        👉 So characters can only move within same parity positions:

        Even indices stay in even
        Odd indices stay in odd

        So instead of simulating swaps, we just need to check:

        ✔ Even index characters match
        ✔ Odd index characters match


        Approach :

        - Create 4 strings:
            - even1, odd1 → for s1
            - even2, odd2 → for s2
        - Traverse both strings:
            - If index is even → add to even string
            - If index is odd → add to odd string
        - Sort all four strings
        - Compare:
            - even1 == even2
            - odd1 == odd2
        - If both match → return true

        Complexity
        Time complexity:
        O(n log n)

        Space complexity:
        O(n)




        '''

        # even1, odd1 = "", ""
        # even2, odd2 = "", ""
        
        # for i in range(len(s1)):
        #     if i % 2 == 0:
        #         even1 += s1[i]
        #         even2 += s2[i]
        #     else:
        #         odd1 += s1[i]
        #         odd2 += s2[i]
        
        # even1 = sorted(even1)
        # even2 = sorted(even2)
        # odd1 = sorted(odd1)
        # odd2 = sorted(odd2)
        
        # return even1 == even2 and odd1 == odd2



        '''

        More optimised 
        '''

        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])
        
        return even_s1 == even_s2 and odd_s1 == odd_s2
        
        


