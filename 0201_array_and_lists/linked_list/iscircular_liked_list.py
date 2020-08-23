from utils.linked_list import LinkedList


def iscircular(linked_list):
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


linked_list = LinkedList()

list1 = [-2, -1, 0, 1, 2]
for v in list1:
    linked_list.append(v)

assert iscircular(linked_list) is False
linked_list.head.next = linked_list.head
assert iscircular(linked_list) is True
