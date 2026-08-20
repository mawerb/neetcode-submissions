class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        q = deque()
        seen = set()
        res=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    seen.add((r,c))

        while q:
            spread=False
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if ((r + nr >= 0 and r + nr < len(grid) and c + nc >= 0 
                        and c + nc < len(grid[0])) and grid[r+nr][c+nc] == 1):
                        grid[r+nr][c+nc] = 2
                        seen.remove((r+nr,c+nc))
                        q.append((r+nr,c+nc))
                        spread=True
            if spread:
                res += 1

        if seen: return -1
        return res
                    