# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root, level):
            if not root:
                return
            if len(result) == level:
                result.append(root.val)
            preorder(root.right, level+1)
            preorder(root.left, level+1)
        preorder(root, 0)
        return result