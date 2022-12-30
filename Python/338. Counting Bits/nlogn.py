class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)

        for i in range(n+1):
            count = 0
            temp = i
            while temp != 0:
                count += (temp & 1)
                temp  = temp >> 1
            result[i] = count

        return result

        #O(nlogn), O(n)