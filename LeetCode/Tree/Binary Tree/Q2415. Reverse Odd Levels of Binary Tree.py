'''
2415. Reverse Odd Levels of Binary Tree
Solved
Medium
Topics
Companies
Hint
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1:


Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation: 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
Example 2:


Input: root = [7,13,11]
Output: [7,11,13]
Explanation: 
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
Example 3:

Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
Explanation: 
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Create a queue using deque for level-order traversal.
        queue = deque([root])
      
        # Initialize a level indicator, starting with level 0 for the root.
        level = 0
      
        # Start the level order traversal of the tree.
        while queue:
            # Temporary list to hold the nodes at the current level.
            current_level_nodes = []
          
            # Iterate over nodes at the current level.
            for _ in range(len(queue)):
                node = queue.popleft()  # Remove the node from the queue.
              
                # If the current level is odd, add the node to the temporary list.
                if level % 2 == 1:
                    current_level_nodes.append(node)
              
                # Add the children of the node to the queue for the next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
          
            # If we have nodes at the current level and the level is odd,
            # reverse the values of the nodes at this level.
            if current_level_nodes:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    # Swap the values of the nodes.
                    current_level_nodes[left].val, current_level_nodes[right].val = current_level_nodes[right].val, current_level_nodes[left].val
                    left += 1
                    right -= 1
          
            # Move to the next level in the tree.
            level += 1
      
        # Return the modified tree.
        return root