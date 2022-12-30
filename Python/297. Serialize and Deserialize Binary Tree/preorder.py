# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def helper(root):
            if not root:
                result.append('N')
                return
            result.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        contain = data.split()
        self.index =0
        def helper():
            if contain[self.index] == 'N':
                self.index += 1
                return
            Node = TreeNode(contain[self.index])
            self.index += 1
            Node.left = helper()
            Node.right = helper()
            return Node
        return helper()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))