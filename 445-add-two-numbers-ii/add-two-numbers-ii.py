# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        l1 = self.revlist(l1)
        l2 = self.revlist(l2)
        while l1 or l2 or carry :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total//10
            curr.next = ListNode(total%10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return self.revlist(dummy.next)




    def revlist(self, ll):
        prev = None
        curr = ll
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev