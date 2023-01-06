import collections
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lookup = {}
        for item in tasks:
            lookup[item] = lookup.get(item, 0) + 1
        hold = []
        for value in lookup.values():
            heapq.heappush(hold, -value)

        time = 0 
        queue = collections.deque()
        
        while hold or queue:
            time += 1

            if hold:
                amount = 1 + heapq.heappop(hold)

                if amount != 0:
                    queue.append([amount, time + n])

            if queue and time == queue[0][1]:
                heapq.heappush(hold, queue.popleft()[0])

        return time
        #O(n * m), O(n)