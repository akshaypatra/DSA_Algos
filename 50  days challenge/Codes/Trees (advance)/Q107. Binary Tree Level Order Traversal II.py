'''

107. Binary Tree Level Order Traversal II
Solved
Medium

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        level order traversal : BFS
        -> will use deque to add new nodes from left to right
        -> res-nested  array to store elements in that level in same array
        -> reversing the res and returning it
        '''

        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]

        while q:
            cur_level=[]
            for _ in range(len(q)):
                node=q.popleft()
                
                cur_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
             
            res.append(cur_level)
        
        return res[::-1]