import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = collections.deque([(root.left, root.right)])

        while queue:
            l, r = queue.popleft()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False

            queue.append((l.left, r.right))
            queue.append((l.right, r.left))

        return True            
        #O(n), O(n)