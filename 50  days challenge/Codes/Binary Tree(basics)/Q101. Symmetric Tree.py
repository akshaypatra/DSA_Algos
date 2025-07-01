'''
101. Symmetric Tree
Solved
Easy
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''

        This solution is not used for checking symmetry
        
        -> Performing inorder (LCR) on left side and 
        -> reversed-inorder (RCL) on right side
        -> if the list matches - return True
        -> else return False



        Working Solution (using DFS) :

        -> check left child of left subtree and right vhild of right subtree 
        -> if they are not equal then return False
        -> else proceed to next nodes 
        -> finally return True if they are same 

        '''

        def DFS(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            
            return DFS(l.left, r.right) and DFS(l.right, r.left)
        
        if (not root.left and not root.right) or not root :
            return True
        
        return DFS(root.left,root.right)
        

            
            




        
            

            
        
