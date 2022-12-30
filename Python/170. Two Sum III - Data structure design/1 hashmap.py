class TwoSum:

    def __init__(self):
        self.contain = {}
        

    def add(self, number: int) -> None: #O(1)
        self.contain[number] = self.contain.get(number, 0) + 1

    def find(self, value: int) -> bool: #O(n), O(n)
        for num in self.contain.keys():
            com = value - num
            if num != com:
                if com in self.contain:
                    return True
            elif self.contain[num] >= 2:
                return True
            
        return False
    


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)