class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')

        for i in range(len(arr)-1):
            min_diff = min(min_diff, arr[i+1] - arr[i])

        result = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])

        return result

        #O(nlogn + n + n), O(n) space for sorting