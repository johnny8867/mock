import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        contain = {}
        result = []
        
        def dfs(root):
            if not root:
                return '#'
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            put = str(root.val) + ',' + left + ',' + right
            
            if put in contain:
                contain[put] += 1
            else:
                contain[put] = 1
            if contain[put] == 2:
                result.append(root)
            return put
        dfs(root)
        return result

        #O(n), O(n)