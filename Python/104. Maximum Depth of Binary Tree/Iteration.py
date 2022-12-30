# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        
        depth = 0
        
        while queue:
            node, deep = queue.popleft()
            
            depth = max(depth, deep)
            
            if node.left:
                queue.append([node.left, deep+1])
            if node.right:
                queue.append([node.right, deep+1])
                
        return depth
    
    #O(N), O(N)