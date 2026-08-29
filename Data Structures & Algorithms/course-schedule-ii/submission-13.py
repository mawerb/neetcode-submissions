class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {course : [] for course in range(numCourses)}

        for cr, pr in prerequisites:
            preMap[cr].append(pr)

        seen = set()
        coursesDone = set()
        res = []

        def dfs(cr):
            if cr in seen:
                return False
            if cr in coursesDone:
                return True
            if not preMap[cr]:
                res.append(cr)
                coursesDone.add(cr)
                return True

            seen.add(cr)

            for pr in preMap[cr]:
                if pr in coursesDone:
                    continue
                if not dfs(pr):
                    return False
                preMap[cr] = []
            seen.remove(cr)
            coursesDone.add(cr)
            res.append(cr)
            return True

        for course in preMap:
            if not dfs(course):
                return []
            
            if len(res) == numCourses:
                return res