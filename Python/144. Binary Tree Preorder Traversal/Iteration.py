# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        contain = []
        cur = root 

        while cur or contain:
            while cur:
                result.append(cur.val)
                contain.append(cur)
                cur = cur.left

            cur = contain.pop()

            cur = cur.right

        return result
        #O(N), O(N)