class Queue:
    def __init__(self, queue_size: int = 10):
        self.arr = [0 for _ in range(queue_size)]
        self.front_index = -1
        self.next_index = 0
        self._size = 0

    def enqueue(self, value):
        if self._size == len(self.arr):
            self._hand_full()

        self.arr[self.next_index] = value
        self._size += 1

        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            self.next_index = 0
            self.front_index = -1
            return None

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self._size -= 1
        return value

    def front(self):
        if self.front_index == -1:
            return None
        return self.arr[self.front_index]

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def _hand_full(self):
        ord_arr = self.arr
        self.arr = [0 for _ in range(2 * len(self.arr))]
        index = 0

        # 复制新一批元素
        for i in range(self.front_index, len(ord_arr)):
            self.arr[index] = ord_arr[i]
            index += 1

        # 复制上一批元素的索引到后一批
        for i in range(0, self.front_index):
            self.arr[index] = ord_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index


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
