class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        next = self.get_next(s)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False

    def get_next(self, s):
        next = [0] * len(s)
        i = 0
        next[0] = 0
        for j in range(1, len(s)):
            while i > 0 and s[j] != s[i]:
                i = next[i - 1]  # 往前退一步
            if s[j] == s[i]:
                i += 1
            next[j] = i

        return next


if __name__ == '__main__':
    so = Solution()
    print(so.repeatedSubstringPattern("abcabcabcabc"))
