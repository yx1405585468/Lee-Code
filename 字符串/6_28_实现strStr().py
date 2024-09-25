from cgitb import reset
from idlelib.debugger_r import restart_subprocess_debugger

from unicodedata import numeric


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力求解法
        # m = len(needle)
        # n = len(haystack)
        # for i in range(n):
        #     if haystack[i:i + m] == needle:
        #         return i
        # return -1



if __name__ == '__main__':
    so = Solution()
    print(so.strStr(haystack="hellol", needle="lo"))
