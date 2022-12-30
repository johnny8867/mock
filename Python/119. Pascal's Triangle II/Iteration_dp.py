class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1] * i for i in range(1, rowIndex+2)]

        for i in range(2, len(rows)):
            for j in range(1, i):
                rows[i][j] = rows[i-1][j] + rows[i-1][j-1]

        return rows[rowIndex]
        #O(n^2), O(n^2)