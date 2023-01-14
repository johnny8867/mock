class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        look_up = {0:-1}

        total = 0

        for i in range(len(nums)):
            total += nums[i]
            mod = total % k

            if mod not in look_up:
                look_up[mod] = i
            elif i - look_up[mod] >= 2:
                return True
        return False
        #O(N), O(N)