# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                self.result += node.val
            helper(node.left)
            helper(node.right)

        helper(root)

        return self.result
        #o(n), O(1)