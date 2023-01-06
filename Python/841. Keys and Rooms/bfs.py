class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)

        queue = deque([0])

        while queue:
            cur = queue.popleft()
            for item in rooms[cur]:
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
                    
        return len(visited) == len(rooms)
        #O(n), O(n)
