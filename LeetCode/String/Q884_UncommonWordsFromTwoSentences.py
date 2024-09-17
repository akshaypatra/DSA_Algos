'''
Leetcode 884 : Uncommon words from two sentences 

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        # Solution 1 : using hashmap

        d={}

        s3=s1+' '+s2
        l1=s3.split(" ")
        

        for i in l1 :
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1

        
        res=[]
        for i in d.keys():
            if d[i]==1:
                res.append(i)
        return res

