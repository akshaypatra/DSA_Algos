'''
102. Binary Tree Level Order Traversal
Solved
Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            Intuition :
                -> Use BFS to traverse tree
                -> cur_level : list of elements of each level
                -> res : append cur_level list after traversng each level
            Beats 100%
            
        '''

        if not root:
            return []

        d=deque()
        res=[]
        
        d.append(root)
        

        while d:
            cur_level=[]
            l=len(d)
            for i in range(l):
                e=d.popleft()
                cur_level.append(e.val)
                if e.left:
                    d.append(e.left)
                if e.right :
                    d.append(e.right)
            res.append(cur_level)
        return res   