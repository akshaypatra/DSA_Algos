'''
206. Reverse Linked List
Solved
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''

        Intuition : Iteratively
        -> using three pointers
                prev_node,
                cur_node,
                next_node

                cur_node.next=prev_node
                prev_node=cur_node
                cur_node=next_node
                next_node=next_node.next
                

        '''
        if not head:
            return head

        next_node=head.next
        prev_node=None
        cur_node=head

        while next_node:
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=next_node
            next_node=next_node.next

        cur_node.next = prev_node

        return cur_node

'''
Recursive solution 

Explanation:
Recursive Call: Move to the next node until we reach the last node (head.next == None).

Backtracking: As recursion unwinds:

Make head.next.next = head to reverse the link.

Set head.next = None to break the old forward connection.

Return New Head: The last node of the original list becomes the new head.

'''
            
class Solution:
    def reverseList(self, head):
        # Base case: If head is None or it's the last node, return head
        if not head or not head.next:
            return head
        
        # Recursive call to reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Reverse the current node’s next pointer
        head.next.next = head  # Point next node’s next to current node
        head.next = None  # Break the original link
        
        return new_head  # Return the new head of the reversed list