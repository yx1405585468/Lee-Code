from unittest.mock import right


def solution(s, num):
    s = s[-num:] + s[:-num]
    return s


if __name__ == '__main__':
    print(solution('abcdefg', 4))
