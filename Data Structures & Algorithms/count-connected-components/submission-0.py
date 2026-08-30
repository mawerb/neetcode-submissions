class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        preMap = { v : [] for v in range(n)}

        for v, e in edges:
            preMap[v].append(e)
            preMap[e].append(v)

        seen = set()
        res = []
        count = 0

        def dfs(v, parent):

            if v in seen or preMap[v] == []:
                return

            seen.add(v)

            for e in preMap[v]:
                if e == parent:
                    continue
                dfs(e, v)
            res.append(v)

            return


        for v in range(n):
            if v in seen:
                continue
            dfs(v, None)

            count += 1
        return count
        


