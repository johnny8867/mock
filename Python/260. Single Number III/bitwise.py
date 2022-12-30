class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitwise = 0
        for item in nums:
            bitwise ^= item

        opp = (~bitwise) + 1
        diff = (bitwise) & opp

        x = 0

        for item in nums:
            if item & diff:
                x ^= item

        return [x, bitwise^x]

        #O(n), O(1)