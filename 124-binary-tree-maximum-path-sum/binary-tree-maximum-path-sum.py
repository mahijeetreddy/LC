# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            left, right = max(left, 0), max(right, 0)
            res[0] = max(root.val + left + right, res[0])
            return root.val + max(left, right)
        dfs(root)
        return res[0]