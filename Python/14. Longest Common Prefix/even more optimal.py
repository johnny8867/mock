class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        strs.sort()

        check = strs[0]

        for i in range(len(check)):
            for j in range(1, len(strs)):
                if check[i] != strs[j][i]:
                    return result
            result += check[i]
        return check
        #O(n * m), n -> number of strings, m -> length of the shorest word in strs (or the longest common prefix)
        #O(n)