class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        contain = [[i for i in range(4)] for i in range(len(startTime))]
        for i in range(len(startTime)):
            contain[i][0] = startTime[i]
            contain[i][1] = endTime[i]
            contain[i][2] = profit[i]
            contain[i][3] = profit[i]

        contain = sorted(contain, key = lambda x: x[1])

        for i in range(1, len(contain)):
            contain[i][3] = max(contain[i][2], contain[i-1][3])
            for j in range(i-1, -1, -1):
                if contain[i][0] >= contain[j][1]:
                    contain[i][3] = max(contain[i][3], contain[i][2] + contain[j][3])
                    break

        return contain[-1][3]
        #O(n^2), O(n)