class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False] * 9 for i in range(9)]
        cols = [[False] * 9 for i in range(9)]
        boxes = [[False] * 9 for i in range(9)]

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == '.':
                    continue
                digit = int(board[y][x]) -1 
                rows[y][digit] = True
                cols[x][digit] = True
                boxes[y//3 * 3 + x//3][digit] = True
        
        self.solver(board, rows, cols, boxes)

    def solver(self, board, rows, cols, boxes):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != '.':
                    continue
                pos = (y//3 * 3 + x // 3)

                for d in range(1,10):
                    if self.isValid(rows, cols, boxes, y, x, pos, d-1):
                        board[y][x] = str(d)
                        rows[y][d-1] = True
                        cols[x][d-1] = True
                        boxes[pos][d-1] = True
                        if self.solver(board, rows, cols,boxes):
                            return True
                        else:
                            board[y][x] = '.'
                            rows[y][d-1] = False
                            cols[x][d-1] = False
                            boxes[pos][d-1] = False
                return False
        return True

    def isValid(self, rows, cols, boxes, r, c, pos, d):
        if rows[r][d] or cols[c][d] or boxes[pos][d]:
            return False
        else:
            return True
    #O(9!)^9, O(3*9*9)