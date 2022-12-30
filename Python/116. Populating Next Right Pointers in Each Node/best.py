"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        node = root
        while root:
            cur = root
            while cur:
                if cur.right:
                    cur.left.next = cur.right
                if cur.next and cur.next.left:
                    cur.right.next = cur.next.left
                cur = cur.next #take care of the right side
            root = root.left #new left subtree
        return node
        #O(n), O(1)