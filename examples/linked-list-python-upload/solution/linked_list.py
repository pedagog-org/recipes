class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, value):
        node = _Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop_front(self):
        if self._head is None:
            raise IndexError("pop from empty list")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def to_list(self):
        out, node = [], self._head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out

    def __len__(self):
        return self._size
