# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if root == p or root == q or not root:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right:
                return root
            return left or right

        result = dfs(root, p, q)

        if result == q:
            return result if dfs(root, p,p) else None
        elif result == p:
            return result if dfs(root, q, q) else None
        return result

        #O(n), O(n)
            