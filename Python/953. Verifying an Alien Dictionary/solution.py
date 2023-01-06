class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        contain_order = {}
        for index, value in enumerate(order):
            contain_order[value] = index

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if contain_order[word1[j]] > contain_order[word2[j]]:
                        return False
                    else:
                        break
        return True
        #O(n), O(n)