class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[0]
        self.stack.pop(0)
        return x

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.peek()
    # queue.pop()
    # queue.empty()
