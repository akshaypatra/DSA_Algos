'''
Leetcode 1367 : Linked List In binary Tree

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

'''

# SOLUTION


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def helper(head,root):
            if head is None:  # Linked list is fully matched
                return True
            if root is None:  # Tree path ends before the list
                return False
            
            if root.val == head.val:  # Current node matches
                # Continue searching in left or right subtree
                if helper(head.next, root.left) or helper(head.next, root.right):
                    return True
            return False  # No match found

        if root is None:  # Tree is empty
            return False

        # Check if the list is a subpath starting at the current root
        # or continue checking in the left or right subtree
        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



            
        

