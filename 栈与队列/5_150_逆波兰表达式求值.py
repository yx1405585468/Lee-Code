from operator import add, mul
from re import sub
from struct import pack_into
from typing import List


def div(x, y):
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int | str:
        stack = []
        op_map = {'+': add, '-': sub, '*': mul, '/': div}
        for i in tokens:
            if i not in {'+', '-', '*', '/'}:
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op_map[i](op1, op2)))
        return int(stack[0])


if __name__ == '__main__':
    so = Solution()
    print(so.evalRPN(tokens=["18"]))
