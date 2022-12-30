# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        contain = set()
        def preorder(node):
            if not node:
                return
            complement = k - node.val
            if complement in contain:
                return True
            contain.add(node.val)
            result = preorder(node.left) or preorder(node.right)
            return result

        return preorder(root)
        #O(n), O(n)