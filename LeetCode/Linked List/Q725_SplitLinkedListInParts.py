'''
Leetcode 725 : SPLIT LINKED LIST IN PARTS

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.



'''

# SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:




        # My first attempt(case2 not running : Attribut AttributeError: 'NoneType' object has no attribute 'next' temp=temp.next)
        # Solved the issue using a if condition and got a optimised solution
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next


        temp=head
        res=[]
        if count<k:
            while temp:
                curr=temp
                res.append(curr)
                temp=temp.next
                curr.next=None
            for i in range(k-count):

                res.append(temp)

        if count%k==0:
            while temp:
                
                res.append(temp)
                for i in range(count//k -1):
                    temp=temp.next
                
                if temp is None:
                    break
                curr=temp
                temp=temp.next
                curr.next=None

        if count%k!=0:
            remaining=count%k

            while temp:
                if remaining>0:
                    remaining-=1
                    
                    res.append(temp)
                    for i in range(count//k):
                        temp=temp.next
                    
                    curr=temp
                    temp=temp.next
                    curr.next=None
                else:
                    
                    res.append(temp)
                    for i in range(count//k-1):
                        if temp is None:
                            break
                        temp=temp.next
                    
                    curr=temp
                    if temp is None:
                            break
                    temp=temp.next
                    curr.next=None
      
        return res



        # SAME CONCEPT using For loop
        
        # length,curr=0,head
        # while curr:
        #     curr=curr.next
        #     length+=1
        
        # base_len,remainder=length//k ,length%k

        # curr=head
        # res=[]

        # for i in range(k):
        #     res.append(curr)



        #     for j in range(base_len + (1 if remainder else 0)):
        #         if not curr:
        #             break
        #         curr=curr.next
        #     remainder-=(1 if remainder else 0)
        #     if curr:

        #         curr.next,curr=None,curr.next
                

        # return res