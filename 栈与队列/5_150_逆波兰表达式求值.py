from struct import pack_into
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int | str:
        stack = []
        for i in tokens:
            if i == "+":
                temp = int(stack[-2]) + int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(temp)
            elif i == "-":
                temp = int(stack[-2]) - int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(temp)
            elif i == "*":
                temp = int(stack[-2]) * int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(temp)
            elif i == "/":
                temp = int(stack[-2]) / int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(temp)
            else:
                stack.append(i)
        return int(stack[0])


if __name__ == '__main__':
    so = Solution()
    print(so.evalRPN(tokens=["18"]))
