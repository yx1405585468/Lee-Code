def sum_zone():
    n = int(input())
    single_list = []
    sum_list = []
    sum = 0
    for i in range(n):
        i = int(input())
        single_list.append(i)
        sum = sum + i
        sum_list.append(sum)
    a = int(input())
    b = int(input())

    print(sum_list[b] - sum_list[a - 1])


if __name__ == '__main__':
    sum_zone()
