class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result = []
        for i in range(len(arr)-1):
            if min_diff > arr[i+1] - arr[i]:
                min_diff = min(min_diff, (arr[i+1]) - arr[i])
                result = [[arr[i], arr[i+1]]]
            elif arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result
        #O(nlogn + n), O(n)