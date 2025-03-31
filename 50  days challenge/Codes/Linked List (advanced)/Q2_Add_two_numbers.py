# 2. Add Two Numbers (Medium)


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]



# Code 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s = ListNode()
        temp = s
        carry = 0

        while l1 or l2 or carry:
            # Getting values from l1 and l2; if None, consider it as 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            temp.val = sum_ % 10

            # Moving l1 and l2 to the next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # Only creating a new node if there's more to process
            if l1 or l2 or carry:
                temp.next = ListNode()
                temp = temp.next

        return s
                    


            