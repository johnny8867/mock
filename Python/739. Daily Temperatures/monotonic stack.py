class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        contain = []
        result = [0] * len(temperatures)

        for index, value in enumerate(temperatures):
            while contain and value > temperatures[contain[-1]]:
                prev_index = contain.pop()
                result[prev_index] = index - prev_index
            contain.append(index)
        return result
        #O(n), O(n)