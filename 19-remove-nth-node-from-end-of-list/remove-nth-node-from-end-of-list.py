# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(head):
            if not head:
                return
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        mainprev = helper(head) #got the reverse:
        
        dummy = ListNode(0)
        dummy.next = mainprev

        prev = dummy
        curr = mainprev

        for _ in range(n-1):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return helper(dummy.next)