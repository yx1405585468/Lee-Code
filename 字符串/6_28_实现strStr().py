import time


class Solution:
    def get_next(self, needle):
        next = [0] * len(needle)
        for j in range(1, len(needle)):
            k = 0
            i = 0
            location = j  # 记录遍历的位置
            while needle[i] == needle[j] and i < j:
                k += 1
                i += 1
                j -= 1
            next[location] = k

        return next
        # s = needle
        # next = [0] * len(needle)
        # j = 0
        # next[0] = 0
        # for i in range(1, len(s)):
        #     while j > 0 and s[i] != s[j]:
        #         j = next[j - 1]
        #     if s[i] == s[j]:
        #         j += 1
        #     next[i] = j
        # return next

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = self.get_next(needle)  # 记录了每个前缀的个数
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


if __name__ == '__main__':
    so = Solution()
    so.strStr(haystack="aabaabaaf", needle="aabaaf")
