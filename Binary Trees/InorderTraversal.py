# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root==None:
            return res
            
        if root.left:
            res+=self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right:
            res+=self.inorderTraversal(root.right)
        return res