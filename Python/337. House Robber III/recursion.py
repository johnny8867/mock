# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)

            with_root = node.val + left[1] + right[1]
            without_root = max(left) + max(right)

            return (with_root, without_root)
        
        return max(helper(root))
        #O(n), O(h)