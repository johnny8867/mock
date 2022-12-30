# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (q and not p) or (not q and p):
            return False
        elif q.val == p.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        #O(n), O(n)