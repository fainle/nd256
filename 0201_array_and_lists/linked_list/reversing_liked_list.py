class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def __iter__(self):
        """
        可迭代对象
        :return:
        """
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        """
        打印
        :return:
        """
        return str([i for i in self])


linked_list = LinkedList()

list1 = [-2, -1, 0, 1, 2]
for v in list1:
    linked_list.append(v)

print(linked_list)
assert list(linked_list) == list1
