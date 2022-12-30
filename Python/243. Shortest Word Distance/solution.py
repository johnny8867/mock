class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        contain = {}
        result = float('inf')
        for i in range(len(wordsDict)):
            contain[wordsDict[i]] = i

            if word1 in contain and word2 in contain and result != abs(contain[word1] - contain[word2]):
                result = min(result, abs(contain[word1] - contain[word2]))
        return result
        #O(n), O(n)