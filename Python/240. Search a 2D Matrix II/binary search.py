class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(min(len(matrix), len(matrix[0]))): #check if m or n is lower.
            row_found = self.binary_search(matrix, target, i, False)
            col_found = self.binary_search(matrix,target, i, True)
            if row_found or col_found:
                return True
        return False

    def binary_search(self, matrix, target, start, search_col):
        low = start
        high = len(matrix[0]) - 1 if search_col else len(matrix) - 1

        while high >= low:
            mid = (low + high) // 2

            if search_col: #search a column, y doesn't change
                if matrix[start][mid] == target:
                    return True
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            else: #search row, x doesn't change
                if matrix[mid][start] == target:
                    return True
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

        #O(log(n!)), O(1)

