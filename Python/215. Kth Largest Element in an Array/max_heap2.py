import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for item in nums:
                heapq.heappush(max_heap, item)

        for _ in range(len(nums)-k):
            heapq.heappop(max_heap)

        return max_heap[0]

       #(nlogn +(len(nums)-k)logn), O(n)

#This method works because the the [0] is guarantee to be the lowest number in the heap