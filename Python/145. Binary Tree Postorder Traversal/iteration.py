# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        contain = []
        result = []
        cur = root

        while contain or cur:
            while cur:
                contain.append((cur, cur.right))
                cur = cur.left

            point = contain.pop()

            if point[1]: #if right exist
                cur = point[1]
                contain.append((point[0], None))
            else:
                result.append(point[0].val)
        return result
        #O(N), O(N)