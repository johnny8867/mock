import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = deque()
        
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            result.append(node.val)
            in_order(node.right)
        in_order(root)

        dummy = start = TreeNode(result[0])
        result.popleft()

        while result:
            cur = result.popleft()
            dummy.right = TreeNode(cur)
            dummy = dummy.right

        return start
        #O(2*N), O(N)
