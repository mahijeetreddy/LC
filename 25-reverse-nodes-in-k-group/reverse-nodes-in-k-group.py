# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)

        tail = dummy
        curr = head
        while curr:
            stack = []
            temp = curr
            for _ in range(k):
                if not temp:
                    tail.next = curr
                    return dummy.next
                stack.append(temp)
                temp = temp.next
            while stack:
                node = stack.pop()
                tail.next = node
                tail = node
            tail.next = temp
            curr = temp
        return dummy.next
