class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self.head

        if index > self.size:
            return -1

        if index == 0:
            return node.value or -1

        while index > 0:
            node = node.next
            index -= 1

        return node.value or -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.head = Node(val)
        self.size = 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val)
            self.size = 1
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(val)
        self.size += 1
        return

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        node = self.head
        length = index if index < self.size else self.size
        for _ in range(length - 1):
            node = node.next
        node.next = Node(val)
        self.size += 1
        return

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """

        if index < 0 or index >= self.size:
            return

        self.size -= 1

        pred = self.head
        for _ in range(index):
            pred = pred.next

        if pred.next is not None:
            pred.next = pred.next.next

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


my_linked_list = MyLinkedList()
my_linked_list.addAtHead(1)
my_linked_list.addAtTail(2)
my_linked_list.addAtTail(3)
my_linked_list.addAtTail(4)
# my_linked_list.print_linked_list()
print()
# print(my_linked_list.size)
# print(my_linked_list.get(5))
my_linked_list.addAtIndex(8, 3)
my_linked_list.addAtIndex(8, 3)
my_linked_list.print_linked_list()
my_linked_list.deleteAtIndex(1)
print()
my_linked_list.print_linked_list()
