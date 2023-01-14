class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        hold = {i: [] for i in range(n)}

        for root, node in edges:
            hold[root].append(node)
            hold[node].append(root)
        visited = set()

        def helper(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for n in hold[node]:
                if n == prev:
                    continue
                if not helper(n, node):
                    return False
            return True
        
        return helper(0, -1) and len(visited) == n
        #O(E+V), O(N)
            