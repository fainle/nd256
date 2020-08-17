class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            return 

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

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


s_linked_list = SinglyLinkedList()
s_linked_list.add(1)
s_linked_list.add(2)
s_linked_list.add(3)
s_linked_list.add(4)
s_linked_list.print_linked_list()
s_linked_list.print_linked_list()
