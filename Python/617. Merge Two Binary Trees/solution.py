# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(p, q):
            if not p and not q:
                return 
            if not p or not q:
                return p or q
            
            if p and q:
                p.val += q.val
            p.left = helper(p.left, q.left)
            p.right = helper(p.right, q.right)
            return p

        return helper(root1, root2)
        #O(n), O(h)