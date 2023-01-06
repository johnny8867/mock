class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for y in range(len(matrix[0])):
            for x in range(len(matrix)):
                result[y][x] = matrix[x][y]

        return result
        #O(n), O(n)