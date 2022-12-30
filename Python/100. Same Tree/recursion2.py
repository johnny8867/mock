# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not q or not p):
            return q == p
        elif (q.val != p.val):
            return False
        else:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

    #O(N), O(N)