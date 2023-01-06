class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        max_val = arr[-1]
        contain = set(arr)
        index = 1
        while True:
            if index not in contain:
                k -= 1
                if k == 0:
                    return index
            index += 1
        #O(n+k), O(n)