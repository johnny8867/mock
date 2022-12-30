class MyHashSet:

    def __init__(self):
        self.contain = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.contain.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.contain:
            self.contain.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.contain:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)