class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            self._size += 1
            return True

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self._size += 1
        return

    def dequeue(self):
        if self.is_empty():
            return None

        node = self.head
        value = node.val
        self.head = node.next
        self._size -= 1
        return value

    def front(self):
        if self.is_empty():
            return None
        return self.head.val

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size


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
    assert queue.front() == 6
