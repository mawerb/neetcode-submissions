class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        LEN = len(board)
        rows,cols,boxes = [set() for _ in range(LEN)], [set() for _ in range(LEN)], [set() for _ in range(LEN)]

        print(rows,cols,boxes)

        for r in range(len(board)):
            for c in range(len(board[r])):
                curr = board[r][c]

                if curr == ".":
                    continue

                boxPos = (r // 3) * 3 + (c // 3)

                if curr in boxes[boxPos] or curr in rows[r] or curr in cols[c]:
                    return False
                
                boxes[boxPos].add(curr)
                rows[r].add(curr)
                cols[c].add(curr)

        return True
                
            