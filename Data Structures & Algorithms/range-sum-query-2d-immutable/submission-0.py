class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m = len(matrix)
        n = len(matrix[0])

        self.prefix_matrix = [[0] * (n + 1) for _ in range(m + 1)]

        prefix_sum = 0

        for row in range(m):
            for col in range(n):
                self.prefix_matrix[row+1][col+1] = (
                    matrix[row][col] +
                    self.prefix_matrix[row][col+1] +
                    self.prefix_matrix[row + 1][col] -
                    self.prefix_matrix[row][col]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_matrix[row2 + 1][col2 + 1]
        diag = self.prefix_matrix[row1][col1]
        left = self.prefix_matrix[row2+1][col1]
        top = self.prefix_matrix[row1][col2+1]

        return total - (left + top - diag)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)