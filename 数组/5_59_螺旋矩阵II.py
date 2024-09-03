import numpy as np


def generateMatrix(n):
    if n <= 0:
        return []
    matrix = [[0] * n for _ in range(n)]  # 初始化矩阵

    # 定义边界
    top = 0
    left = 0
    bottom = n - 1
    right = n - 1

    num = 1

    while top <= bottom and left <= right:
        # 填充top
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # 填充右边
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # 填充底部
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # 填充左边
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1

        left += 1
    print(np.array(matrix))


if __name__ == '__main__':
    generateMatrix(5)
