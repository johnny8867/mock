# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        
        def helper(node, val):
            if not node:
                return 
            
            if node.val >= val:
                self.result += 1

            helper(node.left, max(val, node.val))
            helper(node.right, max(val, node.val))
        helper(root, root.val)

        return self.result
        #O(n), O(h)