# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            
            for i in range(start, end + 1):
                
                left_trees = helper(start, i-1)
                
                right_trees = helper(i+1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        cur = TreeNode(i)
                        cur.left = left
                        cur.right = right
                        all_trees.append(cur)
                        
            return all_trees
        
        return helper(1, n) if n else []
    
    #O(4^n/n^1/2), O(4^n/n^1/2)