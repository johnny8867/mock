class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        contain = []
        for left, right, height in buildings:
            contain.append([left, height])
            contain.append([right, -height])
        contain.sort()

        cur, past = [], []
        result = []
        index = 0

        while index < len(contain):
            cur_x = contain[index][0]

            while index < len(contain) and contain[index][0] == cur_x:
                height = contain[index][1]
                if height > 0:
                    heapq.heappush(cur, -height)
                else:
                    heapq.heappush(past, height)
                index += 1

            while past and past[0] == cur[0]:
                heapq.heappop(past)
                heapq.heappop(cur)
            max_height = -cur[0] if cur else 0

            if not result or result[-1][1] != max_height:
                result.append([cur_x, max_height])

        return result
        #O(NlogN), O(n)
