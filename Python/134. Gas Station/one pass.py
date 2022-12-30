class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        cur_tank = 0
        station = 0

        for i in range(len(gas)):
            total_tank += (gas[i]- cost[i])
            cur_tank += (gas[i] - cost[i])

            if cur_tank < 0:
                station = i + 1
                cur_tank = 0 

        return station if total_tank >= 0 else -1
        #O(N), O(1)