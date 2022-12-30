import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != '.':
                    if board[y][x] in rows[y] or board[y][x] in cols[x] or board[y][x] in boxes[(y//3)*3+ x//3]:
                        return False
                    rows[y].add(board[y][x])
                    cols[x].add(board[y][x])
                    boxes[(y//3)*3+ x//3].add(board[y][x])
        return True
        #O(N^2), O(N^2)