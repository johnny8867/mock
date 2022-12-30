# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            if not root:
                return ''
            s = str(root.val)
            if root.left:
                s += '(' + helper(root.left) + ')'

            if root.right:
                if not root.left:
                    s += '()'
                s += '(' + helper(root.right) + ')'
            return s

        return helper(root)
        #O(n), O(h)