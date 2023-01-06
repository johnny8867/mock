class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                result[x][y] = matrix[y][x]

        return result
        #O(n), O(n)