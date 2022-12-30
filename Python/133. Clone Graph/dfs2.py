"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        contain = {}

        def dfs(node):
            if node in contain:
                return contain[node]

            contain[node] = Node(node.val)

            for nei in node.neighbors:
                contain[node].neighbors.append(dfs(nei))

            return contain[node]

        return dfs(node)
        #O(N + M), N - number of nodes, M - number of edges, O(n)