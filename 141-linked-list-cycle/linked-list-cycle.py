# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l,r = head, head
        while r and r.next:
            
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False


        
        # visit = set()

        # while head and head.next:
        #     if head.next in visit:
        #         return True
        #     visit.add(head.next)

        #     head = head.next


