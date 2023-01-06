class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        for box, unit in boxTypes:
            can_put = min(box, truckSize)
            will_put = can_put * unit
            result += will_put
            truckSize -= can_put
            
            
            if truckSize == 0:
                break

        return result
        #O(nlogn + n), O(1)