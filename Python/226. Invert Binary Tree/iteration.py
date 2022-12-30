import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deque = collections.deque()

        if not root:
            return root
        deque.append(root)
        while deque:
            node = deque.pop()

            node.left, node.right = node.right, node.left

            if node.left: #doesn't matter which to append first.
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return root
        #O(n), O(n)