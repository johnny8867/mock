import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = [] #hi
        self.max_heap = [] #lo
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + (-self.max_heap[0])) /2
        else:
            return self.min_heap[0]

#addNum
#Runtime: O(log n)
#Spacetime: O(n)

#findMedian
#Runtime: O(1)
#Spacetime: O(1)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()