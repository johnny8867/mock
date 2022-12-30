class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = [0] * (len(triangle)+1)

        for item in triangle[::-1]:
            for index, value in enumerate(item):
                rows[index] = value + min(rows[index], rows[index+1])

        return rows[0]