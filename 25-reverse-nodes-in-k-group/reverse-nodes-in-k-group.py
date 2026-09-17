# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        groupPrev = dummy
        def getkth(head, k):
            curr = head
            for _ in range(k):
                if not curr: return None
                curr = curr.next
            return curr
        while True:
            kth = getkth(groupPrev, k)
            if not kth: break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr!= groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next