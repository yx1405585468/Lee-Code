class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif i == '(':
                stack.append(')')
            elif not stack or i != stack[-1]:
                return False
            else:
                stack.pop()
        return True if not stack else False


if __name__ == '__main__':
    so = Solution()
    print(so.isValid(s="{[()]}"))
