class Logger:

    def __init__(self):
        self.contain = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.contain:
            self.contain[message] = timestamp
            return True
        
        if self.contain[message] + 10 <= timestamp:
            self.contain[message] = timestamp
            return True
        
        return False
        
#O(1), #O(m)

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)