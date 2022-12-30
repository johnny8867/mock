"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        contain = {}

        def dfs(node):
            if not node:
                return node
            
            if node in contain:
                return contain[node]
            
            copy = Node(node.val)
            contain[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
        #O(N + M), N - number of nodes, M - number of edges
        #O(N)