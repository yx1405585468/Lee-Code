class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [0]
        for i in range(len(s)):
            if s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        stack.pop(0)
        stack = ''.join(stack)
        return stack


if __name__ == '__main__':
    so = Solution()
    print(so.removeDuplicates(s="aaaaaaaaa"))
