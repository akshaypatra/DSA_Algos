'''
61. Rotate List
Solved
Medium

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        '''
        step 1 : calculate length l of linked list 
        step 2 : if k > length : k = k mod l
        step 3 : make circular linked list (attach the tail to head)
        step 4 : calculate steps   steps = length - k - 1
        step 5 : find new tail by travering i steps.
        step 6 : make the next node after new_tail the new_head
        step 7 : make the new_tail.next = None
        step 7 : return the new head 
        '''

        if not head or not head.next or k == 0:
            return head

        # find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # make circular
        tail.next = head

        # find new tail
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head

            
        