import collections
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hold = collections.defaultdict(str)
        s = s.split()
        if len(pattern) != len(s):
            return False
        seen = set()
        for i in range(len(pattern)):
            if pattern[i] in hold and hold[pattern[i]] != s[i]:
                return False
            elif not hold[pattern[i]] and s[i] in seen:
                return False
            hold[pattern[i]] = s[i]
            seen.add(s[i])

        return True
        #O(N), O(N)

        #need to consider, len
        #if already exist and doesn't equal
        #if value already matched in some other key