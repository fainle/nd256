class Stack:
    def __init__(self, initial_size=10):
        """
        初始化
        :param initial_size:
        """
        self._arr = [0 for _ in range(initial_size)]
        self._size = 0
        self._next_index = 0

    def push(self, value):
        if self._next_index == len(self._arr):
            self._handle_stack()

        self._arr[self._next_index] = value
        self._size += 1
        self._next_index += 1

    def pop(self):
        if self.is_empty():
            self._next_index = 0
            return None

        self._size -= 1
        self._next_index -= 1

        return self._arr[self._next_index]

    def is_empty(self):
        return True if not self._size else False

    def size(self):
        return self._size

    def top(self):
        return self._arr[self._next_index - 1]

    def _handle_stack(self):
        old_arr = self._arr
        self._arr = [0 for _ in range(2 * len(old_arr))]
        for index, value in enumerate(old_arr):
            self._arr[index] = value


if __name__ == '__main__':
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(0)
    assert stack.is_empty() is False
    for i in range(10):
        stack.push(i)
    assert stack.size() == 11
    assert stack.pop() == 9
    assert stack.pop() == 8
