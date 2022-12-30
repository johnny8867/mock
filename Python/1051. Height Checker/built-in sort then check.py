class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        
        if sorted_heights == heights:
            return 0

        count = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                count +=1

        return count

        #O(nlogn + n), O(n)