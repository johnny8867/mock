class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for item in zip(*strs):
            print(len(item))
            if len(set(item)) == 1:
                result += item[0]
            else:
                break
        return result
        #O(n), O(n)