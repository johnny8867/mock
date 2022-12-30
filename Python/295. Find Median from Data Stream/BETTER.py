import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] #max_heap
        self.right = [] #min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.left and self.right and (-self.left[0] > self.right[0]): #ensure that the max left val always < min right val
            val = - heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        #uneven case
        if len(self.left)+1 < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

        if len(self.left) > len(self.right)+1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        return (self.right[0] + (-self.left[0])) / 2

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