class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        result = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                if max_left - height[left] > 0:
                    result += (max_left - height[left])
            else:
                right -= 1
                max_right = max(max_right, height[right])
                if max_right - height[right] > 0:
                    result += (max_right - height[right])

        return result

        #O(n), O(1)