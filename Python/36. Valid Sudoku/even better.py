import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * len(board[0]) for i in range(len(board))]
        cols = [[False] * len(board[0]) for i in range(len(board))]
        boxes = [[False] * len(board[0]) for i in range(len(board))]

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != '.':
                    val = int(board[y][x]) - 1
                    if rows[y][val] or cols[x][val] or boxes[(y//3)*3+ x//3][val]:
                        return False
                    rows[y][val] = True
                    cols[x][val] = True
                    boxes[(y//3)*3+ x//3][val] = True
        return True
        #O(N^2), O(N^2)