#19. Remove Nth Node From End of List
#Given the head of a linked list, remove the nth node from the end of the list and return its head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0, head)

        
        prev=dummy
        curr=head

        for i in range(n):
            curr=curr.next
            

        while curr is not None:
            prev=prev.next
            curr=curr.next
        prev.next=prev.next.next

        return dummy.next
