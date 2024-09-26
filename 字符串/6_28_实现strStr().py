import time


class Solution:
    def get_next(self, needle):

        s = needle
        next = [0] * len(needle)
        i = 0
        next[0] = 0
        for j in range(1, len(s)):
            while i > 0 and s[j] != s[i]:
                i = next[i - 1]  # 往前退一步
            if s[j] == s[i]:
                i += 1
            next[j] = i

        return next

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
    so.strStr(haystack="aabaabaar", needle="aabaaf")
