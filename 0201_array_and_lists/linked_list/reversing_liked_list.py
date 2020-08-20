from utils.linked_list import LinkedList


def reverse(linked_list):
    tail_pos = linked_list.head
    reversed_linked_list = LinkedList()

    if tail_pos is None:
        return None

    while tail_pos:
        value = tail_pos.value
        reversed_linked_list.prepend(value)
        tail_pos = tail_pos.next

    return reversed_linked_list


linked_list = LinkedList()

list1 = [-2, -1, 0, 1, 2]
for v in list1:
    linked_list.append(v)

assert list(linked_list) == list1
assert list(reverse(linked_list)) == list(reversed(list1))
