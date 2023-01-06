class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hold = {}
        result = 0
        for song in time:
            remain = song % 60
            if remain != 0:
                result += hold.get(60 - remain, 0)
            else:
                result += hold.get(0, 0)
            hold[remain] = hold.get(remain, 0) + 1
        return result
        #O(N), O(N)