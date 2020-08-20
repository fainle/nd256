class Node(object):
    """
    单链表
    """

    def __init__(self, value):
        self.value = value
        self.next = None


def pring_linked_list(node):
    """
    打印链表
    :param node:
    :return:
    """
    current_node = node
    s = ''
    while current_node is not None:
        print(str(current_node.value) + ' -> ', end='')
        current_node = current_node.next


def create_linked_list(input_list):
    try:
        head = Node(input_list.pop(0))
        tail = head

        while len(input_list):
            tail.next = Node(input_list.pop(0))
            tail = tail.next

    except IndexError:
        head = None

    return head


def create_linked_list_better(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next

    return head


head = create_linked_list([1, 2, 3, 7, 5, 6, 7, 8])
head2 = create_linked_list_better([1, 2, 3, 7, 5, 6, 7, 8])
pring_linked_list(head)
print('\n')
pring_linked_list(head2)
