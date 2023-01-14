class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_change = set() #set makes it unique and slight optimal for solution
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    to_change.add((y,x))

        while to_change:
            yy, xx = to_change.pop()
            for i in range(len(matrix)):
                matrix[i][xx] = 0
            for i in range(len(matrix[0])):
                matrix[yy][i] = 0
        #O(n), O(n)