class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permuteUnique(nums)

            for item in perms:
                item.append(n)
                if item not in result:
                    result.append(item)

            nums.append(n)

        return result

        #O(N*N!), O(N!)