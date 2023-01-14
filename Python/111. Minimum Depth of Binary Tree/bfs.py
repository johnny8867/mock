import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque()
        queue.append([root, 1])

        while queue:
            cur_root, val = queue.popleft()

            if not cur_root.left and not cur_root.right:
                return val
            
            if cur_root.left:
                queue.append([cur_root.left, val + 1])
            if cur_root.right:
                queue.append([cur_root.right, val + 1])
        #O(N), O(N)
