import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.contain = nums
        self.k = k
        heapq.heapify(self.contain)

        while len(self.contain) > k:
            heapq.heappop(self.contain)
    #O(nlogn), O(N)

    def add(self, val: int) -> int:
        if len(self.contain) < self.k:
            heapq.heappush(self.contain, val)
        else:
            heapq.heappushpop(self.contain, val)
        return self.contain[0]

        #(logk), O(1)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)