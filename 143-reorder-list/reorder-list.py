# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        def reverse(head):
            if not head: return None
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        second = reverse(second)
        first, second = head, second

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        

        