class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])
        
        return self.merge(left_list, right_list)
        
    def merge(self, left_list, right_list):
        left = right = 0
        result = []
        while left < len(left_list) and right < len(right_list):
            if left_list[left] < right_list[right]:
                result.append(left_list[left])
                left += 1
            else:
                result.append(right_list[right])
                right += 1
                
        result.extend(left_list[left:] or right_list[right:])
        
        return result
    
            #O(NlogN), O(N)