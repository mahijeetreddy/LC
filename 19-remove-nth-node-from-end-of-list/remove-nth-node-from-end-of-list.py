# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if not head:
            return None
        rever = reverse(head)

        if n == 1:
            rever = rever.next
        else:
            curr = rever
            for _ in range(n-2):
                curr = curr.next
            curr.next = curr.next.next
        return reverse(rever)
        
