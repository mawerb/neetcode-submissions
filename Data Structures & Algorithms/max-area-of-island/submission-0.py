class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        res = 0

        def dfs(row,col):
            if (row < 0 or row == len(grid) or col < 0 
                or col == len(grid[0]) or (row,col) in seen or grid[row][col] == 0):
                return 0

            seen.add((row,col))

            return 1 + dfs(row,col+1) + dfs(row,col-1) + dfs(row+1,col) + dfs(row-1,col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if ((row,col) in seen):
                    continue
                elif grid[row][col] == 1:
                    area = dfs(row,col)
                    if area > res:
                        res = area
            
        return res