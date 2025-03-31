'''
21. Merge Two Sorted Lists
Solved
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
      
        # Current node is used to keep track of the end of the merged list
        current = sentinel
      
        # Iterate while both lists have nodes
        while list1 and list2:
            # Choose the smaller value from either list1 or list2
            if list1.val <= list2.val:
                current.next = list1   # Append list1 node to merged list
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2   # Append list2 node to merged list
                list2 = list2.next     # Move to the next node in list2
          
            # Move the current pointer forward in the merged list
            current = current.next
      
        # Add any remaining nodes from list1 or list2 to the merged list
        # If one list is fully traversed, append the rest of the other list
        current.next = list1 if list1 else list2
      
        # The sentinel node's next pointer points to the head of the merged list
        return sentinel.next
