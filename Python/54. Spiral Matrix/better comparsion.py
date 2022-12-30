class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        result = []

        while len(result) < len(matrix) * len(matrix[0]):
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1

            if  len(result) == len(matrix) * len(matrix[0]):
                break
            
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1,-1):
                result.append(matrix[i][left])
            left += 1
        return result
        #O(M*N), O(N)