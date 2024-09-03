def main():
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    sum = 0
    vec = []
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
            # 遍历到行末尾时候开始统计
            if j == m - 1:
                result = min(result, abs(sum - 2 * count))

    count = 0
    # 列切分
    for j in range(m):

        for i in range(n):
            count += vec[i][j]
            # 遍历到列末尾时候开始统计
            if i == n - 1:
                result = min(result, abs(sum - 2 * count))

    print(result)


if __name__ == "__main__":
    main()
