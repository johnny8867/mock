class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        for i in range(k):
            val = nums.pop()
            nums.insert(0,val)
        #O(N), O(1)?
        