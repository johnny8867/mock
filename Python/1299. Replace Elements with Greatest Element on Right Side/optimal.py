class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1

        for i in range(len(arr)-1, -1, -1):
            val = arr[i]
            arr[i] = cur_max
            cur_max = max(val, cur_max)

        return arr
        #O(N), O(1)