class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self._size = 0
        self.head = None

    def push(self, value):
        node = self.head
        if node is None:
            self.head = Node(value)
            self._size += 1
            return

        add_node = Node(value)
        add_node.next = self.head
        self.head = add_node
        self._size += 1

    def pop(self):
        node = self.head
        if node is None:
            return None

        pop = self.head
        self.head = self.head.next
        self._size -= 1
        return pop.value

    def is_empty(self):
        return True if not self.head else False

    def size(self):
        return self._size

    def top(self):
        if self.head is None:
            return None

        return self.head.value


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
