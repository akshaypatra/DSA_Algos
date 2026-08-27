'''
144. Binary Tree Preorder Traversal
Solved
Easy

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        '''
        Approach 1 : Recursive 

        root -> left -> right
        '''

        # res=[]
        # self.helper(root,res)
        # return res


        '''
        Approach 2 : Iterative with stack

        stack = [1,2,4,5,6,7,3,8,9]
        '''

        stack =[root]
        res=[]

        if not root :
            return res


        while stack :
            node = stack.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
            
            res.append(node.val)
        return res


    def helper(self,root,res):
        if root :
            res.append(root.val)
            self.helper(root.left,res)
            self.helper(root.right,res)
