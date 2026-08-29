class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        if not prerequisites:
            return True

        paths = defaultdict(list)

        for course, prereq in prerequisites:
            paths[course].append(prereq)

        seen = set()
        possible = set()

        def dfs(course):
            if course not in paths or course in possible:
                possible.add(course)
                return True
            if course in seen:
                return False

            seen.add(course)

            for prereq in paths[course]:
                if not dfs(prereq):
                    return False
            possible.add(course)
            return True

        for course in paths:
            if dfs(course) == False:
                return False
        return True