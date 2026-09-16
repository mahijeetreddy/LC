# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        output = []
        def inorder(root):
            nonlocal output
            if not root: return None
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
            return output
        
        inorder(root)
        return output[k-1]