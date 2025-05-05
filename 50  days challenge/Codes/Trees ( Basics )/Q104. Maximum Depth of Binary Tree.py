'''

104. Maximum Depth of Binary Tree
Solved
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Depth First Search


        '''
        # def dfs(node,current_height):
        #     if not node:
        #         return current_height
            
            
        #     current_height=max(dfs(node.left,current_height+1),dfs(node.right,current_height+1))

            
        #     return current_height
        
        # return dfs(root,0)


        '''
        Optimised code
        '''

        # if not root:
        #     return 0

        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))


        '''
        Breath First Search

        '''
        if not root:
            return 0
        
        level=0
        q=deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level


            
        

