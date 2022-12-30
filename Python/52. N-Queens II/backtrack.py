class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        self.result = 0

        def backtrack(r):
            if r == n:
                self.result += 1
                return 

            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)

        backtrack(0)
        return self.result
        #O(N*N!) I think?, O(N)