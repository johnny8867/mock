class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if changed:
                    return False

                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                changed = True
        return True
        #O(N), O(1)