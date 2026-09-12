"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oc = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oc[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oc[cur]
            copy.next = oc[cur.next]
            copy.random = oc[cur.random]
            cur = cur.next
        return oc[head]