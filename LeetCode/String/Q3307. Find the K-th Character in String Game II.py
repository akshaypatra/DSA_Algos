'''
3307. Find the K-th Character in String Game II
Solved
Hard

Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.

Now Bob will ask Alice to perform all operations in sequence:

If operations[i] == 0, append a copy of word to itself.
If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word after performing all the operations.

Note that the character 'z' can be changed to 'a' in the second type of operation.

 

Example 1:

Input: k = 5, operations = [0,0,0]

Output: "a"

Explanation:

Initially, word == "a". Alice performs the three operations as follows:

Appends "a" to "a", word becomes "aa".
Appends "aa" to "aa", word becomes "aaaa".
Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".
Example 2:

Input: k = 10, operations = [0,1,0,1]

Output: "b"

Explanation:

Initially, word == "a". Alice performs the four operations as follows:

Appends "a" to "a", word becomes "aa".
Appends "bb" to "aa", word becomes "aabb".
Appends "aabb" to "aabb", word becomes "aabbaabb".
Appends "bbccbbcc" to "aabbaabb", word becomes "aabbaabbbbccbbcc".
 

Constraints:

1 <= k <= 1014
1 <= operations.length <= 100
operations[i] is either 0 or 1.
The input is generated such that word has at least k characters after all operations.

'''

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        '''
        Bruteforce : travsersal and performing operations
        -> TL exceeded : 737/901 test cases passed
        '''
        # s="a"
        # for i in operations:
        #     if i==0:
        #         s+=s
        #     else:
        #         for c in range(len(s)):
        #             s+=chr(ord(s[c])+1)
        #     if len(s)>=k:
        #         break
        # return s[k-1]


        '''
        optimization - 
        -> operationsCount = ceil(taking log2 of the k)
        -> increases contains the number of times a is incremented
        -> loop from i=operationsCount to 0
        -> halfSize=i**2
        -> if k>halfSize then. (reducing k till we get the poper breakpoint of the string)
                -> k-=halfSize
                -> increses+=operations[i]
        -> return character having ascii value (increases % 26)


        '''

        operationsCount=math.ceil(math.log2(k))
        increases=0

        for i in range(operationsCount,-1,-1):
            halfSize=2**i
            if k>halfSize:
                k-=halfSize
                increases+=operations[i]
            
        return string.ascii_letters[increases%26]

