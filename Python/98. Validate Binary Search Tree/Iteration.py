# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -float('inf'), float('inf'))]

        while stack:
            cur, lower, upper = stack.pop()
            if not root:
                continue
            if lower >= cur.val or cur.val >= upper:
                return False
            if cur.left:
                stack.append((cur.left, lower, cur.val))
            if cur.right:
                stack.append((cur.right, cur.val, upper))

        return True
        #O(N), O(N)