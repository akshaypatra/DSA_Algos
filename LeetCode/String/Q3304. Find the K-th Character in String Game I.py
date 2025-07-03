'''

3304. Find the K-th Character in String Game I
Solved
Easy

Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Example 2:

Input: k = 10

Output: "c"

 

Constraints:

1 <= k <= 500

'''

class Solution:
    def kthCharacter(self, k: int) -> str:
        '''
        ASCII Values of Characters :

        a - 97
        z - 122

        ord() to get ascii val of character
        chr() to convert asci to characeter

        '''
        # BruteForce Solution : 
        # -> Simple Traversal and adding next alphabet till length reaches k

        str_len=1
        s="a"

        while len(s)<=k:
            for i in range(len(s)):
                if s[i]!='z':
                    s+=chr(ord(s[i])+1)
                else:
                    s+='a'
                str_len+=1
        return s[k-1]


        #Optimized Solution : 
        # As constraint is very small i.e K<=500

        # ans = 0
        # while k != 1:
        #     t = k.bit_length() - 1
        #     if (1 << t) == k:
        #         t -= 1
        #     k -= 1 << t
        #     ans += 1
        # return chr(ord("a") + ans)


        
