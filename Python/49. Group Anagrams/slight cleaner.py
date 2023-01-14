import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hold = collections.defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            hold[key].append(word)

        return hold.values()
        #O(NMlog(M)), O(NM) n- word in input, m max length of string in input