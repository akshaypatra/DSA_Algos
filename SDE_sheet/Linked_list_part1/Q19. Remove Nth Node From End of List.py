'''

19. Remove Nth Node From End of List
Solved
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Approach 1 : Bruteforce

        - traverse the linked list to find the number of nodes 
        - again traverse the Linked list to get to ith position ie. {len(linked_list) - n} th position 
        - when (i-1)th position is reached , point its (i-1)th pointer to (i)th next  .

        Edge cases :

        - when LL has only one node 
        - when i-1 th position is None .
        - when i+1 the position is None .

        TC : O(n)
        SC : O(1)

        '''

        # cur=head
        # size = 0
        # while cur :
        #     size+=1
        #     cur=cur.next
        
        # if size == 1 and n == 1 :
        #     return None
        
        # position = size - n 

        # if position == 0 :
        #     return head.next
        
        # cur=head
        # c=0
        # while cur :
            
        #     if c == position - 1:
        #         cur.next = cur.next.next
        #         break
        #     cur=cur.next
        #     c+=1
        

        # return head


        '''
        Approach 2 : Two Pointers -> Slow and Fast pointer (One pass solution):

        Algo :

        🚀 Approach
            - Initialize Pointers: Both ptr (fast) and temp (slow) start at the head.
            - Create the Gap: Move the ptr forward times.
            - Advance Together: Move both ptr and temp forward one step at a time until ptr reaches the last node (ptr.next == null).
            - Edge Case - Removing Head: If after creating the gap, ptr is already null, it means we need to remove the first node of
              the list. We return head.next.
            - Delete Node: Change the next pointer of the temp node to skip the target node: temp.next = temp.next.next.
            
        ⚙️ Dry Run Analogy (important): 

            Imagine two people walking. Person A starts walking and gets a head start of meters. Then Person B starts walking at the 
            same speed. When Person A hits the wall at the end of the hallway, Person B is exactly meters away from that wall.


        TC : O(n)
        SC : O(1)

        '''


        ptr = temp = head

        # move forward ptr n times
        for _ in range(n):
            ptr = ptr.next
        
        # if ptr is at null it means 
        if not ptr :
            return head.next

        # move the temp and ptr at the same time
        #  when ptr reaches end -> temp is n position behind

        while ptr.next:
            temp=temp.next
            ptr=ptr.next
        
        temp.next=temp.next.next
        return head

        

        







            



        
