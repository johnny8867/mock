import random
class RandomizedSet:

    def __init__(self):
        self.table = set()

    def insert(self, val: int) -> bool:
        result = val not in self.table
        if result:
            self.table.add(val)
        return result

    def remove(self, val: int) -> bool:
        result = val in self.table
        if result:
            self.table.remove(val)
        return result
        

    def getRandom(self) -> int:
        return random.sample(self.table, 1)[0]

    #O(1), O(N) for set


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()