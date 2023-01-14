class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_parent(n1):
            res = n1

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1,n2)
        
        return result
        # O(n log n), O(n)