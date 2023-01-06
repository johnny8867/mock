class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0

        if low % 2 == 1 or high %2 == 1:
            result += 1

        result += (high - low) // 2

        return result
        #O(1), O(1)