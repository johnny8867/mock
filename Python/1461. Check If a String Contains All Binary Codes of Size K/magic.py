class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hash_set = set()

        for i in range(k, len(s)+1):
            if s[i-k:i] not in hash_set:
                hash_set.add(s[i-k:i])

        return len(hash_set) == 2 ** k

        #O(N*K), O(N)