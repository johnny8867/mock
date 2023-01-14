class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        result = [-1] * len(arr)

        cur_max = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            cur_max = max(cur_max, arr[i+1])

            result[i] = cur_max

        return result
        #O(N), O(N)