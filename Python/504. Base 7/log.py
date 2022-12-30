class Solution:
    def convertToBase7(self, num: int) -> str:
        value = abs(num)

        result = ''

        while value != 7:
            result =  str(value % 7) + result
            value //= 7

        if value >= 0:
            result = str(value) + result

        if num < 0:
            return '-' + (result)
        return result
        #O(logn), O(1)