def isAnagram(s, t):
    # 首先小写字母的ASCII是连续的，a-z的码为x ~ x+26
    # 所以定义一个长度为26的数组，意味着任何一个字母的ASCII码 - a的码 后 不会超过26
    record = [0] * 26

    for i in s:
        record[ord(i) - ord('a')] += 1  # ord(i) - ord('a') 这个距离其实就可以作为i的位置

    for i in t:
        record[ord(i) - ord('a')] -= 1  # 同样的位置做累减操作

    # 遍历record表，如果里面的值有不为0的，说明s和t的字符，肯定有不一样的
    for i in range(26):
        if record[i] != 0:
            return False
    return True


if __name__ == '__main__':
    s = 'fuckyou'
    t = 'youfuck'
    print(isAnagram(s, t))
