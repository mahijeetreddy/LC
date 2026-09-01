# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y): #12, 4
            while y:
                x,y = y, x%y
            return x

        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            nxt = head.next
            gcdnode = ListNode(gcd(head.val, head.next.val))
            head.next = gcdnode
            gcdnode.next = nxt
            head = nxt
        return dummy.next
        
