import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contain = {}
        for item in nums:
            contain[item] = contain.get(item, 0) + 1

        heap = []
        for key, value in contain.items():
            heapq.heappush(heap, (value,key))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for i in range(k-1,-1,-1):
            result.append(heap[i][1])

        return result

        #O(n + nlogk + n), O(k+n)