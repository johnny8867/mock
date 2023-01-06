class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        contain = {}

        for item in items:
            if item[0] not in contain:
                contain[item[0]] = [item[1]]
            else:
                contain[item[0]].append(item[1])

        result = []

        for key, value in contain.items():
            if len(value) >= 5:
                value.sort()
                result.append([key, sum(value[-5:])//5])
            else:
                result.append([key, sum(value)/len(value)])

        result.sort()

        return result
        #O(n + n* value*logn(value) + n), O(n)