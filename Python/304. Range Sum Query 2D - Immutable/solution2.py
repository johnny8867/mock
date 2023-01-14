class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]

        for y in range(1, len(self.dp)):
            for x in range(1, len(self.dp[0])):
                val = matrix[y-1][x-1]
                self.dp[y][x] = val + self.dp[y-1][x] + self.dp[y][x-1] - self.dp[y-1][x-1]
        #O(N^2), O(N)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        res += self.dp[row2 + 1][col2 + 1]
        res -= self.dp[row1][col2 + 1]
        res -= self.dp[row2 + 1][col1]
        res += self.dp[row1][col1]
        return res
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)