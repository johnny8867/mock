class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]

        for y in range(1, len(self.dp)):
            prefix = 0
            for x in range(1, len(self.dp[0])):
                above = self.dp[y-1][x]
                prefix += matrix[y-1][x-1] #becaue y, x starts at 1, so -1 to offset to original matrix
                self.dp[y][x] = prefix + above
        #O(N^2), O(N)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        top_left = self.dp[row1-1][col1-1]
        bottom_left = self.dp[row2][col1-1]
        top_right = self.dp[row1-1][col2]
        result = self.dp[row2][col2]
        #O(1), O(1)
        return result - top_right - bottom_left + top_left
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)