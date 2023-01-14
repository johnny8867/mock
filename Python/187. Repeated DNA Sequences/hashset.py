class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeat = set()
        seen = set()

        for i in range(10, len(s)+1):
            word = s[i-10:i]
            if word in seen:
                repeat.add(word)
            seen.add(word)

        return repeat
        #O(N), O(N)