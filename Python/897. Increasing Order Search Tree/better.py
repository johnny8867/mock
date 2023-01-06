import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.cur = self.result = TreeNode(0)

        def in_order(node):
            if not node:
                return
            in_order(node.left)

            self.result.right = TreeNode(node.val)
            self.result = self.result.right
            in_order(node.right)
        in_order(root)

        return self.cur.right
        #O(N), O(N)
