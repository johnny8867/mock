"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#(same as 117)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()

                if i < size - 1:
                    print(size-1, queue[0].val)
                    cur.next = queue[0]

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root
        #O(n), O(n)