class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            val = nums.pop(0)
            
            perms = self.permute(nums)

            for item in perms:
                item.append(val)
                result.append(item)

            nums.append(val)
        return result
        #O(N*N!)? #O(N!)