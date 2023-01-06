class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid <= k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k
        #O(logn), O(1)
        #why does this work?