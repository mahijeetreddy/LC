# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge2(list1, list2):
            dummy = ListNode(0)
            tail = dummy
            curr1 , curr2 = list1, list2
            while curr1 and curr2:
                if curr1.val<= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next
                tail = tail.next
            tail.next = curr1 or curr2
            return dummy.next

        for i in range(len(lists) -1):
            lists[i+1] = merge2(lists[i], lists[i+1])

        return lists[-1]