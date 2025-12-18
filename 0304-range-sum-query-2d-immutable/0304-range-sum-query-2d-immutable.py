class NumMatrix:

    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            row_sum = 0
            for c in range(1, n + 1):
                row_sum += matrix[r - 1][c - 1]
                self.pre[r][c] = self.pre[r - 1][c] + row_sum

    def sumRegion(self, row1, col1, row2, col2):
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (self.pre[r2][c2]
                - self.pre[r1 - 1][c2]
                - self.pre[r2][c1 - 1]
                + self.pre[r1 - 1][c1 - 1])



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 0  1  2  3  4 
# 3  3  4  8  10
# 15 21 24 26 27 

