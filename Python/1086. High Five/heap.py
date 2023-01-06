import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        contain = {}

        for item in items:
            if item[0] not in contain:
                temp = []
                heapq.heappush(temp, item[1])
                contain[item[0]] = temp
            else:
                if len(contain[item[0]]) >= 5:
                    heapq.heappushpop(contain[item[0]], item[1])
                else:
                    heapq.heappush(contain[item[0]], item[1])

        result = []

        for key, value in contain.items():
            if len(value) != 5:
                result.append([key, sum(value)//len(value)])
            else:
                result.append([key, sum(value)//5])

        return sorted(result)
        #O(nlogn + n), O(n)