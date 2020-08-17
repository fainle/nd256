class Node:
    """
    节点结构
    """

    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    """
    基础链表
    """

    def __init__(self):
        self.head = None

    def prepend(self, value):
        """
        追加节点到头部
        :param value:
        :return:
        """
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        new_node = Node(value)
        new_node.next = node
        self.head = new_node

        return

    def append(self, value):
        """
        追加到尾部
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

    def search(self, value):
        """
        搜索值所在到第一个节点
        :param value:
        :return:
        """
        node = self.head
        if node is None:
            return None

        while node:
            if value == node.value:
                return node

            if node.next is None:
                return None

            node = node.next

        return

    def remove(self, value):
        """
        移掉指定数据
        :param value:
        :return:
        """
        position_prev_tail = None
        position_tail = self.head

        while position_tail:
            if value == position_tail.value:
                # 如果上一级节点为空 则为头节点
                if position_prev_tail is None:
                    self.head = position_tail.next
                    return
                else:
                    # 当前的下一节移给上一级
                    position_prev_tail.next = position_tail.next
                    return

            position_prev_tail = position_tail  # 当前变成上一级
            position_tail = position_tail.next  # 开始便利下一个

        return

    def pop(self):
        """
        弹出第一个的值
        :return:
        """
        node = self.head
        if node is None:
            return None

        self.head = node.next
        return node.value or None

    def insert(self, value, pos):
        """
        插入值到指定位置
        :param value:
        :param pos:
        :return:
        """
        position_tail = self.head

        if pos == 0:
            position_next = self.head
            self.head = Node(value)
            self.head.next = position_next
            return

        for _ in range(pos):
            if position_tail.next is None:
                position_tail.next = Node(value)
                return

            position_tail = position_tail.next

        position_next = position_tail.next
        add = Node(value)
        add.next = position_next
        position_tail.next = add

        return

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def size(self):
        s = 0
        node = self.head

        while node:
            s += 1
            node = node.next

        return s

# 测试用例
linked_list = LinkedList()

# Test prepend
linked_list.prepend(1)
assert linked_list.to_list() == [1]
linked_list.prepend(2)
linked_list.prepend(3)
# print(linked_list.to_list())
assert linked_list.to_list() == [3, 2, 1]

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1]
linked_list.append(2)
assert linked_list.to_list() == [1, 2]

# Test search
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
assert linked_list.search(2).value == 2
assert linked_list.search(3).value == 3
assert linked_list.search(7) is None

# Test Remove
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(1)
linked_list.append(2)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.remove(1)
assert linked_list.to_list() == [1, 2, 2, 3, 4]
linked_list.remove(4)
assert linked_list.to_list() == [1, 2, 2, 3]
linked_list.remove(2)
assert linked_list.to_list() == [1, 2, 3]

# Test pop
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

value = linked_list.pop()
assert value == 1
assert linked_list.head.value == 2

# Test Insert
linked_list = LinkedList()
linked_list.insert(1, 0)
assert linked_list.to_list() == [1]
linked_list.insert(2, 1)
assert linked_list.to_list() == [1, 2]
linked_list.insert(3, 4)
assert linked_list.to_list() == [1, 2, 3]

# Test size()
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
assert linked_list.size() == 3

