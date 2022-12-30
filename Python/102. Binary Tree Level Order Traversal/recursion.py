# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        contain = []

        def helper(root, level):
            if not root:
                return
 
            if len(contain) == level:
                contain.append([])

            contain[level].append(root.val)
            
            helper(root.left, level+1)
            helper(root.right, level+1)

        helper(root, 0)

        return contain     

        #(N), O(N)