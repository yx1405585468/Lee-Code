def isHappy(n: int) -> bool:
    record = set()
    while n not in record:
        record.add(n)
        new_num = 0
        n_str = str(n)  #将正整数n转为字符串，这样子方便对每一位取值
        for i in n_str:
            new_num += int(i) ** 2
        if new_num == 1:
            return True
        else:
            n = new_num
    return False


if __name__ == '__main__':
    print(isHappy(99))
