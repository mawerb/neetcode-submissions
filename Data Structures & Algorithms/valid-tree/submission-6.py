class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True
        
        preMap = { v : [] for v in range(n) }


        for v, e in edges:
            preMap[v].append(e)
            preMap[e].append(v)

        seen = set()
        res = []

        def dfs(v, parent):
            if v in seen:
                return False
            if preMap[v] == []:
                return True

            seen.add(v)

            for edge in preMap[v]:
                if edge == parent:
                    continue

                if not dfs(edge,v):
                    return False

            seen.remove(v)
            res.append(v)
            preMap[v] = []

            return True

        for v in range(n):
            if not dfs(v, None):
                return False
            if len(res) == n:
                return True
            res = []

        return False
