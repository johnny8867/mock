import collections
class Solution:
    def romanToInt(self, s: str) -> int:
        contain = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        hold = collections.deque()
        for item in s:
            hold.append(item)

        while hold:
            val = hold.popleft()
            print(hold)
            if val == 'I' and hold and hold[0] == 'V':
                hold.popleft()
                result += 4
            elif val == 'I' and hold and hold[0] == 'X':
                hold.popleft()
                result += 9
            elif val == 'X'and hold and hold[0] == 'L':
                hold.popleft()
                result += 40
            elif val == 'X' and hold and hold[0] == 'C':
                hold.popleft()
                result += 90
            elif val == 'C' and hold and hold[0] == 'D':
                hold.popleft()
                result += 400
            elif val == 'C' and hold and hold[0] == 'M':
                hold.popleft()
                result += 900
            else:
                result += contain[val]
        return result
        #O(n), O(n)