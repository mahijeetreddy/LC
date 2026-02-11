"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            nxt = None
            prev = None
            while cur:
                for child in (cur.left, cur.right):
                    if child:
                        if not nxt:
                            nxt = child
                        if prev:
                            prev.next = child
                        prev = child
                cur = cur.next
            cur = nxt
        return root