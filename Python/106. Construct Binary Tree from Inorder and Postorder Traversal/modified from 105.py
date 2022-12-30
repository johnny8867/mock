# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.root_index = len(postorder) - 1
        inorder_dict = {value:index for index, value in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return
            root_val = postorder[self.root_index]
            self.root_index -= 1
            Node = TreeNode(root_val)

            in_order_index = inorder_dict[root_val]
            
            Node.right = helper(in_order_index+1, right)
            Node.left = helper(left, in_order_index-1)
            
            return Node

        return helper(0, len(inorder)-1)
        #O(n), O(n)