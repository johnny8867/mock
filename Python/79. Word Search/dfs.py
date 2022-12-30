class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > (len(board)*len(board[0])):
            return False
        
        contain_board = {}
        contain_word = {}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                contain_board[board[i][j]]= contain_board.get(board[i][j], 0) + 1
                
        for char in word:
            contain_word[char] = contain_word.get(char, 0) + 1
        
        for key in word:
            if key not in contain_board or contain_word[key] > contain_board[key]:
                return False
    #end of preprocessing to pass testcase
        visited = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r,c) not in visited and board[r][c] == word[i]:
                visited.add((r,c))
                res = dfs(r-1,c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
                visited.remove((r,c))
            else:
                return False
            return res

        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(y,x,0):
                    return True
        return False
        #(n*m*4^n), O(N)