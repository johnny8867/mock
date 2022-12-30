import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        
        for item in nums:
            heapq.heappush(max_heap, item)

        for _ in range(len(nums)- k+1):
            result = heapq.heappop(max_heap)

        return result

        #(nlogn +(len(nums)-k)logn), O(n)