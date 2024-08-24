# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.

# Example 1:

# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters in word are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0
# Explanation:
# No character in word appears in uppercase.

# Example 3:
# Input: word = "abBCab"
# Output: 1
# Explanation:
# The only special character in word is 'b'.


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # working code (not efficient)
        # s=set(word)
        # count=0
        # for i in s:
        #     if i.islower() and (i.upper() in s):
        #         count+=1
        # return count
        

        #  using hashmap (reduced space complexity but  time complexity is not optimised)

        # d={}
        # s=set(word)
        # w=list(s)
        # w.sort()
        # for i in w:
        #     if i.isupper() :
        #         d[i]=0
        #     if i.islower() and (i.upper() in d.keys()):
        #         d[i.upper()]+=1
        # count=0
        # for i in d.keys():
        #     if d[i]>=1:
        #         count+=1
        # return count
        

        # optimised code
        from string import ascii_lowercase # ascii lowercase contains all lowercase alphabets
        word = set(word)
        res = 0

        for i in ascii_lowercase:
            if (i in word) and (i.upper() in word):
                res += 1


        return res




        
