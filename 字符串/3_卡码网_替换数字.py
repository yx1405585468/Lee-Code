class Solution:
    def change(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i].isdigit():
                s[i] = "number"
        return ''.join(s)


if __name__ == '__main__':
    so = Solution()
    print(so.change('a1b2c3'))
