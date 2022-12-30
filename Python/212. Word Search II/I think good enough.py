class Trie:
    def __init__(self):
        self.contain = {}
        self.end = False

    def addword(self, word):
        cur = self
        for char in word:
            if char not in cur.contain:
                cur.contain[char] = Trie()
            cur = cur.contain[char]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root_list = Trie()
        result = set()
        visited = set()
        for word in words:
            root_list.addword(word)

        def dfs(r,c, root, word):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited and board[r][c] in root.contain:
                visited.add((r,c))
                root = root.contain[board[r][c]]
                word += board[r][c]

                if root.end:
                    result.add(word)
                    root.end = False

                dfs(r-1, c, root, word)
                dfs(r+1, c, root, word)
                dfs(r, c-1, root, word)
                dfs(r, c+1, root, word)
                visited.remove((r,c))
            
        to_check = [item[0] for item in words]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in to_check:
                    dfs(r, c, root_list, "")
                
        return list(result)

#O(m*n*4^(m*n))


        