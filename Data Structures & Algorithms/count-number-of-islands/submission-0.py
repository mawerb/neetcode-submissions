class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0

        def dfs(row,col):
            if (row < 0 or row == len(grid) or col < 0 
            or col == len(grid[0]) or (row,col) in seen):
                return
            
            seen.add((row,col))

            if (grid[row][col] == "0"):
                return

            dfs(row,col+1)
            dfs(row,col-1)
            dfs(row+1,col)
            dfs(row-1,col)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) in seen:
                    continue
                elif grid[row][col] == "1":
                    dfs(row,col)
                    res += 1
                else:
                    seen.add((row,col))

        return res

