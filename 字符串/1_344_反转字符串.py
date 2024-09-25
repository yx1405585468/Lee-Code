from typing import List


class Solution:
    # 双指针
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

    # 栈
    def reverseString(self, s: List[str]) -> List[str]:
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()
        return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    # s = ["H", "a", "n", "n", "a", "h"]
    so = Solution()
    print(so.reverseString(s))
