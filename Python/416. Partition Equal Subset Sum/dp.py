class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            contain = set()
            for item in dp:
                if nums[i] + item == target:
                    return True
                contain.add(nums[i] + item)
                contain.add(item)
            dp = contain

        return True if target in dp else False
        #O(2^N), O(N)

