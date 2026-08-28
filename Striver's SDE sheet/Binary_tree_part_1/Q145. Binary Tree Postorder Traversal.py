'''
145. Binary Tree Postorder Traversal
Solved
Easy

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        Approach 1 : Recursive solution

        left -> right -> root
        '''

        # res = []
        # self.helper(root,res)
        # return res

        '''
        Approach 2 : Iterative solution using Stack and visit stack

        -> to append to res , the node should be visited twice
        -> TC : O(n)
        -> SC : O(n)
        '''
        stack = [root]
        visit = [False]
        res = []

        while stack :
            cur,v = stack.pop(),visit.pop()

            if cur :
                if v :
                    res.append(cur.val)
                else :
                    stack.append(cur)
                    visit.append(True)

                    # append cur.right first and then left -> in next iteration left is poped first
                    stack.append(cur.right)
                    visit.append(False)

                    stack.append(cur.left)
                    visit.append(False)
        return res

    def helper(self,node,res):

        if node :
            self.helper(node.left,res)
            self.helper(node.right,res)
            res.append(node.val)
        

