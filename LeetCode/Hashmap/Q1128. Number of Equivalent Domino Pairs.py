'''

1128. Number of Equivalent Domino Pairs
Solved
Easy

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9

'''

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        d = defaultdict(int)
        count = 0
        for i, j in dominoes:
            key = tuple(sorted((i, j)))  # Normalize the key
            count += d[key]
            d[key] += 1
        return count
                













        '''
        BruteForce : O(n^2) Solution - Time limit exceeded

        '''
        
        count=0
        for i in range(len(dominoes)-1):
            for j in range(i+1,len(dominoes)):
                if (dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1]) or (dominoes[i][0]==dominoes[j][1] and dominoes[i][1]==dominoes[j][0]):
                    count+=1
        return count