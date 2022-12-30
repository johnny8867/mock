class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def divide_c(left, right,up, down):
            if left > right or up > down:
                return False

            if target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = (left + right) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return divide_c(left, mid-1, row,down) or divide_c(mid+1, right, up,row-1)

        return divide_c(0, len(matrix[0])-1, 0, len(matrix)-1)

        #O(nlogn), O(logn)