# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        contain = []
        def dfs(root, level):
            if not root:
                return
            if len(contain) == level:
                contain.append([])
            contain[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return [item[-1] for item in contain]
        #O(n), O(n)