# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []
        def helper(node):
            if not node:
                result.append('N')
                return
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ' '.join(result)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        contain = data.split()
        self.index = 0
        def helper():
            if contain[self.index] == 'N':
                self.index += 1
                return None
            node = TreeNode(int(contain[self.index]))
            self.index += 1
            node.left = helper()
            node.right = helper()

            return node
        return helper()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans