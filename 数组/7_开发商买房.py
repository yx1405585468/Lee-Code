def main():
    # 输入数据
    data = input().split()

    # 读取n行
    idx = 0
    n = int(data[idx])

    # 读取m列
    idx += 1
    m = int(data[idx])

    # 计算权重总值
    idx += 1
    vec = []
    sum = 0

    # 做二维数组
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])
            idx += 1
            row.append(num)
            sum += num
        vec.append(row)
    print(vec)
    print(sum)
    result = float('inf')
    count = 0
    # 行切分
    for i in range(n):
        for j in range(m):
            count += vec[i][j]
            if j == m - 1:
                result = min(result, abs(sum - count * 2))

    # 列切分
    count = 0
    for j in range(m):
        for i in range(n):
            count += vec[i][j]
            if i == n - 1:
                result = min(result, abs(sum - count * 2))

    print(result)


if __name__ == '__main__':
    main()
