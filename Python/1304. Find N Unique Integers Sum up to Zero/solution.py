class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(-(n//2), (n//2)+1):
            if i == 0:
                continue
            result.append(i)

        if n % 2 == 1:
            result.append(0)

        return result
        #O(n), O(n)