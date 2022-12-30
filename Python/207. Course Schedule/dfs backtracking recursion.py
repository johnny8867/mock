class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        contain = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            contain[course].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if contain[course] == []:
                return True
            
            visited.add(course)
            for item in contain[course]:
                if not dfs(item):
                    return False
            contain[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        #O(N + P), O(N)