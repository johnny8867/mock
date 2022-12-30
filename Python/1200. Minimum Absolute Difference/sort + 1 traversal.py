class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        result = []
        for i in range(len(arr)-1):
            cur_diff = arr[i+1] - arr[i]

            if cur_diff == min_diff:
                result.append([arr[i], arr[i+1]])
            elif cur_diff < min_diff:
                result = [[arr[i], arr[i+1]]]
                min_diff = cur_diff

        return result

        #O(nlogn + n), O(n)