# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_val = root.val
        
        while root:
            if abs(root.val - target) < abs(min_val - target):
                min_val = root.val
            
            elif root.val > target:
                root = root.left
            else:
                root = root.right
                
                
        return min_val
    
    #O(H), O(1)
                