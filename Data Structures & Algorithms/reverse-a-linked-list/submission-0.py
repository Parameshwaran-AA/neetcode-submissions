# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        current = head

        while(current):

            # we are storing the next node here to reuse
            next_node = current.next

            # Then now to pick up the current_next node and map it to prev node 
            current.next = prev

            # keeping the previous element is current 
            prev = current

            # and then we need to change the current element 
            current = next_node
        
        return prev



        