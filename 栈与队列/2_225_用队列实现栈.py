class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        x = self.stack[-1]
        self.stack.pop(-1)
        return x

    def top(self) -> int:
        if self.empty():
            return None
        return self.stack[-1]

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False


if __name__ == '__main__':
    obj = MyStack()
    obj.push(6)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
