# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.contain = []
        self.index = 0
        self.dfs(root)
        print(self.contain)

    def next(self) -> int:
        val = self.contain[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.contain)

    def dfs(self, root):
        if not root:
            return root
        self.dfs(root.left)
        self.contain.append(root.val)
        self.dfs(root.right)
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()