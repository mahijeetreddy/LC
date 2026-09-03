# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2(l1, l2):
            if not l1 and not l2:
                return None
            curr1, curr2 = l1, l2
            dummy = ListNode(0)
            tail = dummy
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next
                tail = tail.next
            tail.next = curr1 or curr2
            return dummy.next

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    merged.append(merge2(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])

            lists = merged
        return lists[0] if lists else None