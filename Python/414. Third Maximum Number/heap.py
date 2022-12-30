import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        contain = []

        for item in nums:
            heapq.heappush(contain, -item)

        result = contain[0]

        if len(nums) < 3:
            return -result
        else:
            for i in range(3):
                result = -heapq.heappop(contain)
            return result
        #O(n + 3logn), O(n)