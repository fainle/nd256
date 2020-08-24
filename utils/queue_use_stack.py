from utils.stack import Stack


class Queue:
    def __init__(self):
        self.stack = Stack()

    def enqueue(self, value):
        self.stack.push(value)
        return True

    def dequeue(self):
        stack1 = Stack()
        stack2 = Stack()

        # 通过两个栈 反转栈 得到第一个
        for _ in range(self.stack.size() - 1):
            stack1.push(self.stack.pop())

        for _ in range(stack1.size()):
            stack2.push(stack1.pop())

        value = self.stack.pop()  # 弹出第一个
        self.stack = stack2
        return value

    def is_empty(self) -> bool:
        return self.stack.size()

    def size(self) -> int:
        return self.stack.size()


if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 11):
        queue.enqueue(i)

    assert queue.size() == 10
    queue.dequeue()  # 1
    queue.dequeue()  # 2
    queue.dequeue()  # 3
    queue.dequeue()  # 4
    queue.enqueue(11)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)
    queue.enqueue(15)
    assert queue.size() == 11
    assert queue.dequeue() == 5
