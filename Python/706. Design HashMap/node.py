class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.contain = [None] * self.size
    
    def hashkey(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hashkey(key)
        
        if self.contain[index] == None:
            self.contain[index] = Node((key, value))
            return
        
        current = self.contain[index]

        while current:
            k, v = current.val
            if k == key:
                current.val = (key, value)
                return
            else:
                if current.next == None:
                    current.next = Node((key, value))
            current = current.next

    def get(self, key: int) -> int:
        index = self.hashkey(key)

        if self.contain[index] == None:
            return -1
        
        current = self.contain[index]

        while current:
            if current.val[0] == key:
                return current.val[1]
            current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hashkey(key)

        if self.contain[index] == None:
            return 
        
        current = self.contain[index]

        dummy = Node((0,0))
        dummy.next = current
        cur = dummy
        while dummy and dummy.next:
            if dummy.next.val[0] == key:
                dummy.next = dummy.next.next
            dummy = dummy.next
        self.contain[index] = cur.next

        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)