# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val == right.val:
                return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right)
        #O(n), O(n)