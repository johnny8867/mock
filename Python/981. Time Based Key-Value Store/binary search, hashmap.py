class TimeMap:

    def __init__(self):
        self.contain = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.contain:
            self.contain[key] = [[value, timestamp]]
        else:
            self.contain[key].append([value, timestamp])
        #O(1)

    def get(self, key: str, timestamp: int) -> str:
        hold = self.contain.get(key, [])

        left = 0
        right = len(hold) - 1
        result = ''

        while left <= right:
            mid = (left + right) // 2
            if hold[mid][1] == timestamp:
                return hold[mid][0]
            elif hold[mid][1] < timestamp:
                result = hold[mid][0]
                left = mid + 1
            else:
                right = mid -1 
        return result
        #O(logn), O(1)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)