# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = root.val
        diff = abs(result - target)
        while root:
            if diff > abs(root.val - target):
                diff = abs(root.val - target)
                result = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
            print(result)
        return result
        #O(n), O(1)