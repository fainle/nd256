class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init=None):
        self.head = None
        if init:
            for v in init:
                self.append(v)

    def append(self, value):
        """
        前面追加
        :param value:
        :return:
        """
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def prepend(self, value):
        """
        后面追加
        :param value:
        :return:
        """
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        add_node = Node(value)
        add_node.next = node
        self.head = add_node
        return

    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def reverse(self):
        node = self.head
        reversed_linked_list = LinkedList()

        while node:
            value = node.value
            node = node.next
            reversed_linked_list.prepend(value)

        return reversed_linked_list

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
        return

    def __repr__(self):
        return str([i for i in self])


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    linked_list = LinkedList(list1)

    assert list(linked_list) == list1
    assert linked_list.size() == 5

    linked_list.prepend(0)
    assert list(linked_list) == [0] + list1

    assert list(linked_list.reverse()) == list(reversed([0] + list1))

