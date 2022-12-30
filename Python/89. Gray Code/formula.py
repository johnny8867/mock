class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):
            print(i)
            result.append(i ^ ( i >> 1))

        return result

        #O(2^n), O(1)