# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(0,head)
        front = back = dummy


        # now we need to keep the front until it is moved n number of times
        for i in range (n):
            front = front.next
            

        # here we need to find the prev element of the deletion node 
        while(front.next):
            front = front.next
            back = back.next
            
        back.next = back.next.next
        

        return dummy.next
    