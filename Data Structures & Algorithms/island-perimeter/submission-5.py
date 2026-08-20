class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        init_i, init_j = -1, -1
        found_land = False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    init_i, init_j = row, col
                    found_land = True
                    break
            if found_land:
                break

        visited = set()

        def dfs_land(i, j):

            if ((i,j) in visited):
                return 0

            if i == len(grid) or i < 0 or j == len(grid[0]) or j < 0 or grid[i][j] == 0:
                return 1
            
            visited.add( (i,j) )

            return dfs_land(i-1,j) + dfs_land(i,j-1) + dfs_land(i,j+1) + dfs_land(i+1,j)

        return dfs_land(init_i, init_j)
