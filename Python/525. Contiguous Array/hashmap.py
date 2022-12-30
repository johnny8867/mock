class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        contain = {}
        cur_sum = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
            
            if cur_sum == 0:
                result = i+1
            elif cur_sum in contain.keys():
                result = max(result, i - contain[cur_sum])
            else:
                contain[cur_sum] = i
        return result
        #O(N), O(N)