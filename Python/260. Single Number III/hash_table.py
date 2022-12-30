class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        look_up = {}
        for item in nums:
            look_up[item] = look_up.get(item, 0) + 1

        result = []
        for key, value in look_up.items():
            if value == 1:
                result.append(key)

        return result

        #O(n), O(n)
