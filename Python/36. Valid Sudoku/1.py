class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == '.':
                    continue
                if board[y][x] in rows[y] or board[y][x] in cols[x] or board[y][x] in square[(y//3,x//3)]:
                    return False
                
                rows[y].add(board[y][x])
                cols[x].add(board[y][x])
                square[(y//3,x//3)].add(board[y][x])
                
        return True
    
    #O(n^2), O(n^2)