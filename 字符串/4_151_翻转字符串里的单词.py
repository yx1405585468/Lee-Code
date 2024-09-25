class Solution:
    def reverseWords(self, s: str) -> str:
        # python做法
        s = s.strip()
        s = s[::-1].split()
        s = ' '.join(x[::-1] for x in s)
        return s

        # 双指针用法
        s = s.split()
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        s = ' '.join(s)
        return s


if __name__ == '__main__':
    so = Solution()
    s = "the sky is blue"
    print(so.reverseWords(s))
