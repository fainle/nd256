from utils.stack import Stack


class Queue:
    def __init__(self):
        self._arr = []

    def enqueue(self, value):
        self._arr.append(value)
        return True

    def dequeue(self):
        return self._arr.pop(0)

    def is_empty(self) -> bool:
        return len(self._arr) == 0

    def size(self) -> int:
        return len(self._arr)


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
