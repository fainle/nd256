class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


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
        """
        反转链表
        :return:
        """
        node = self.head
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        self.head = prev
        return

    def check_loops(self):
        node = self.head
        if node is None:
            return False

        slow = node
        fast = node

        if fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def even_after_odd(self):
        pass

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
        return

    def __repr__(self):
        return str([i for i in self])


def merge(node1=None, node2=None):
    if node1 is None:
        return node2
    elif node2 is None:
        return node1
    elif node1.value < node2.value:
        node1.next = merge(node1.next, node2)
        return node1
    else:
        node2.next = merge(node1, node2.next)
        return node2


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    linked_list = LinkedList(list1)

    assert list(linked_list) == list1
    assert linked_list.size() == 5

    linked_list.reverse()
    assert list(linked_list) == list(reversed(list1))

    assert linked_list.check_loops() is False
    linked_list.head.next = linked_list.head
    assert linked_list.check_loops() is True

    list1 = [1, 3, 5]
    linked_list = LinkedList(list1)
    list2 = [2, 4, 6]

    new_linked = merge(linked_list.head, LinkedList(list2).head)
    new_list = []
    while new_linked:
        new_list.append(new_linked.value)
        new_linked = new_linked.next

    assert new_list == [1, 2, 3, 4, 5, 6]

    linked_list.even_after_odd()
