class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1) #dp
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            result[i] = result[i - offset] + 1

        return result

        #O(n), O(1)