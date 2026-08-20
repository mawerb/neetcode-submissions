class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))


        while queue:
            r,c = queue.popleft()

            for nr, nc in [(0,1), (0,-1), (1,0), (-1,0)]:
                cr, cc = r + nr, c+ nc

                if (cr > -1 and cr < len(grid)
                    and cc > -1 and cc < len(grid[0]) and grid[cr][cc] == 2147483647
                    ):

                    grid[cr][cc] = grid[r][c] + 1
                    queue.append((cr,cc))