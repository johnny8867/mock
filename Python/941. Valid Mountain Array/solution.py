class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index = 0

        while index < len(arr) - 1: #skipping the last one
            if arr[index] == arr[index+1]:
                return False
            if arr[index] < arr[index+1]:
                index += 1
            else:
                break

        if index == 0 or index+1 == len(arr):
            return False

        while index < len(arr) - 1: #skipping the last one
            if arr[index] == arr[index+1]:
                return False
            if arr[index] > arr[index+1]:
                index += 1
            else:
                break
        return index+1 == len(arr)
        #O(n), O(1)