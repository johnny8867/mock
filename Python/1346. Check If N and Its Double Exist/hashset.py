class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        contain = set(arr)
        for item in arr:
            if item != 0 and item * 2 in contain:
                return True

        return False