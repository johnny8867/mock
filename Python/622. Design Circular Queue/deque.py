import collections
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.contain = collections.deque()

    def enQueue(self, value: int) -> bool:
        if len(self.contain) == self.k:
            return False
        self.contain.append(value)
        return True
        
    def deQueue(self) -> bool:
        if not self.contain:
            return False
        self.contain.popleft()
        return True

    def Front(self) -> int:
        if not self.contain:
            return -1
        return self.contain[0]
        
    def Rear(self) -> int:
        if not self.contain:
            return -1
        return self.contain[-1]
        
    def isEmpty(self) -> bool:
        return len(self.contain) == 0

    def isFull(self) -> bool:
        return len(self.contain) == self.k
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()