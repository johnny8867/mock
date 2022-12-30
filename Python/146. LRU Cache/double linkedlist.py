class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.contain = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head    

    def insert(self, node) -> None:
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node


    def remove(self, node) -> None:
        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev


    def get(self, key: int) -> int:
        if key in self.contain:
            self.remove(self.contain[key])
            self.insert(self.contain[key])
            return self.contain[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.contain:
            self.remove(self.contain[key])

        self.contain[key] = Node(key, value)
        self.insert(self.contain[key])

        if len(self.contain) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            self.contain.pop(lru.key)
#O(1), O(1)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)