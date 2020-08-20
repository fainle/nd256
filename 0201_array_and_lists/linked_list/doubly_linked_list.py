class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

        return

    def print_linked_list(self):
        current_node = self.head
        if current_node:
            print(str(current_node.value), end='')
        else:
            print('None')

        while current_node and current_node.next:
            print(' -> ', str(current_node.next.value), end='')
            current_node = current_node.next
        print()


linked_list = DoublyLinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.print_linked_list()