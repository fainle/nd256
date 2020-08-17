class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


matrix1 = [
              [1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
          ],

target1 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
s = Solution()

assert s.rotate(matrix=matrix1) == target1
