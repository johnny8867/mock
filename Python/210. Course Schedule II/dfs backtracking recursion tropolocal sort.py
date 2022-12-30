class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        contain = {i:[] for i in range(numCourses)}
        visited = set()
        good = set()
        result = []
        for index, course in prerequisites:
            contain[index].append(course)
        
        def dfs(course):
            if course in visited:
                return False
            elif course in good:
                return True

            visited.add(course)
            for item in contain[course]:
                if not dfs(item):
                    return False
            good.add(course)
            visited.remove(course)
            result.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
        #O(n+p), O(n)
