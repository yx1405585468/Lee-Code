def canConstruct(str1: str, str2: str) -> bool:
    magazine = dict()
    for i in str2:
        if i not in magazine:
            magazine[i] = 1
        else:
            magazine[i] += 1

    for j in str1:
        if j not in magazine:
            return False
        else:
            if magazine[j] == 0:
                return False
            else:
                magazine[j] = magazine[j] - 1
    return True


if __name__ == '__main__':
    print(canConstruct("aabv", 'aaba'))
