class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        contain = []
        for index, val in enumerate(mat):
            count = 0
            for i in range(len(mat[0])):
                if val[i] == 0:
                    break
                count += 1
            contain.append((count,index))

        contain.sort()

        result = []

        for i in range(k):
            result.append(contain[i][1])

        return result

        #(n^2 + nlogn + k)
        #O(n)