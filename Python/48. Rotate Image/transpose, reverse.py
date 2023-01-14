class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for y in range(len(matrix)):
            for x in range(y, len(matrix[0])):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        for row in matrix:
            row.reverse()
        
        #O(N^N + N), O(1)