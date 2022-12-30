import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for item in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, item)

            else:
                heapq.heappushpop(min_heap, item)

        return min_heap[0]

        #O(nlogk), O(k)