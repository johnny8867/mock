class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findlow(nums, target):
            res = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        def findhigh(nums, target):
            res = -1
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        return [findlow(nums, target), findhigh(nums, target)]
        #O(logn), O(1)
