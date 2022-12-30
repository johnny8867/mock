import collections
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        contain = {}
        queue = collections.deque([node])

        if not node:
            return node

        while queue:
            cur = queue.popleft()

            if cur in visited:
                continue
            visited.add(cur)

            if cur not in contain:
                contain[cur] = Node(cur.val)

            for nei in cur.neighbors:
                if nei not in contain:
                    contain[nei] = Node(nei.val)
                contain[cur].neighbors.append(contain[nei])
                queue.append(nei)

        return contain[node]
        #O(n), O(n)

