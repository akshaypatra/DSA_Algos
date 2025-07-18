'''

110. Balanced Binary Tree
Solved
Easy

Given a binary tree, determine if it is height-balanced.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Height balanced Tree :  difference of heights of left subtree and right subtree should not be more than 1 

        Intuition :
            -> using recursion (returning the max-height) and at every step finding the diffence between the 
                max height returned by both left and right nodes
            -> also using flag to denote the res
        '''
        self.flag=True
        def dfs(node):
            
            if not node:
                return 0
            
            left_h=dfs(node.left)
            right_h=dfs(node.right)
            if abs(left_h-right_h)>1:
                self.flag=False

            max_height=max(left_h,right_h)

            return max_height+1
        
        
        dfs(root)
        return self.flag


        '''
        Without flag
        '''

        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     left = dfs(node.left)
        #     if left == -1:
        #         return -1
            
        #     right = dfs(node.right)
        #     if right == -1:
        #         return -1
            
        #     if abs(left - right) > 1:
        #         return -1
            
        #     return max(left, right) + 1
        
        # return dfs(root) != -1