class Trie():
    def __init__(self):
        self.contain = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.contain:
                cur.contain[char] = Trie()
            cur = cur.contain[char]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(index, root):
            cur = root
            for i in range(index, len(word)):
                char = word[i]

                if char == '.':
                    for value in cur.contain.values():
                        if dfs(i+1, value):
                            return True
                    return False
                elif char in cur.contain:
                    cur = cur.contain[char]
                else:
                    return False
            return cur.end
        return dfs(0, self.root)
        #O(N*26^N), O(M)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)