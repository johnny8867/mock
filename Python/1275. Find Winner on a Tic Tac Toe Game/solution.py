class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        player = 1
        n = 3
        row = [0] * n
        col = [0] * n
        pos_diag = 0
        neg_diag = 0

        for r,c in moves:
            row[r] += player
            col[c] += player

            if r == c:
                pos_diag += player

            if (r+c) == n-1:
                neg_diag += player
            
            if abs(row[r]) == n or abs(col[c]) == n or abs(pos_diag) == n or abs(neg_diag) == n:
                if player == 1:
                    return 'A'
                else:
                    return 'B'
            player *= -1

        if len(moves) == n*n:
            return 'Draw'
        return 'Pending'
        #O(N), O(1)