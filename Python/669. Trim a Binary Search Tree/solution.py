# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return
            if root.val < low:
                return helper(root.right)
            if root.val > high:
                return helper(root.left)

            root.left = helper(root.left)

            root.right = helper(root.right)

            return root

        return helper(root)
        #O(n), O(1)