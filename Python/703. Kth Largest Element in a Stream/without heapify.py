import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.contain = []

        for item in nums:
            if self.k > len(self.contain):
                heapq.heappush(self.contain, item)
            elif len(self.contain) >= self.k:
                heapq.heappushpop(self.contain, item)

    #O(nlogk), O(k)

    def add(self, val: int) -> int:
        if self.k > len(self.contain):
            heapq.heappush(self.contain, val)
        elif len(self.contain) >= self.k:
            heapq.heappushpop(self.contain, val)

        return self.contain[0]
    #O(logk), O(1)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)