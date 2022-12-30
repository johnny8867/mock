class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0 
        ori = heights[:]
        for i in range(len(heights)-1,-1,-1):
            for j in range(i):
                if heights[j] > heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        
        for i in range(len(ori)):
            if heights[i] != ori[i]:
                count += 1

        return count

        #O(n^2 + n), O(n)