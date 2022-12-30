"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        self.first = None
        self.last = None

        self.in_order(root)
        self.first.left = self.last
        self.last.right = self.first

        return self.first

    def in_order(self, node):
        if node:
            self.in_order(node.left)

            if not self.first:
                self.first = node
            else:
                self.last.right = node
                node.left = self.last
            self.last = node

            self.in_order(node.right)

    #O(N), O(log N) for balanced tree, O(N) for unbalanced tree

