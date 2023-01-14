import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hold = {i: [] for i in range(n)}

        for start, end in edges:
            hold[start].append(end)
            hold[end].append(start)

        visited = set()

        def bfs(val):
            queue = collections.deque([val])

            while queue:
                node = queue.popleft()
                visited.add(node)

                for nei in hold[node]:
                    if nei not in visited:
                        queue.append(nei)
        result = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                result += 1
        return result
        #O(E+V), O(N)