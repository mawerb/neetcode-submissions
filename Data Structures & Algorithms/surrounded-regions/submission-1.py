class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        sides = set()

        def dfs(r,c):
            if (r,c) in sides or r < 0 or r == ROWS or c < 0 or c == COLS:
                return

            if board[r][c] == "X":
                return
            
            sides.add((r,c))

            for nr,nc in [(1,0),(-1,0),(0,1),(0,-1)]:
                cr,cc = r + nr, c + nc

                dfs(cr,cc)

        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            dfs(r,0)
            dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in sides:
                    board[r][c] = "X"