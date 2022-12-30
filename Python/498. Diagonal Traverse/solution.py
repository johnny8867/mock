class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        contain = {}
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if (x+y) not in contain:
                    contain[x+y] = [mat[y][x]]
                else:
                    contain[x+y].append(mat[y][x])

        result = []

        for key, value in contain.items():
            if key % 2:
                result += value
            else:
                result += value[::-1]

        return result 
        #O(n), O(n)