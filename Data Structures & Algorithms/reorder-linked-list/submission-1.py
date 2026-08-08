# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        fast = head.next
        slow = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None
        prev = None
        while(current):
            next_node = current.next
            current.next = prev
            prev = current
            current= next_node
        
        # Here I will make the zip
        
        first = head
        second = prev
        while (first and second):
            f_next = first.next
            s_next = second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next
        


            

        


        