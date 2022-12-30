class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1] * i for i in range(1,numRows+1)]
        for i in range(2, len(rows)):
            for j in range(1,i):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]

        return rows
        #O(N^2), O(n^2)