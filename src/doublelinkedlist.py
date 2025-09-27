class Node:
    previous: object = None
    value: int = 0
    next: object = None

    def __init__(self,
                 previous: object=None,
                 value:int = 0,
                 next: object=None):
        self.previous = previous
        self.value = value
        self.next = next

class DoubleLinkedList:
    head: Node = None
    tail: Node = None
    _length: int = 0

    def append(self, new_val: int) -> None:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        new_node = Node(value=new_val)
        if self._length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self._length += 1

    def prepend(self, new_val: int) -> None:
        """
        Time complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(value=new_val)
        if self._length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self._length += 1

    def pop_left(self) -> None:
        """
        Time complexity: O(1)
        Space Complexity: O(1)
        """
        if self._length == 0:
            return
        elif self._length == 1:
            self.head = self.tail = None
        else:
            next_node = self.head.next
            self.head.next = next_node.previous = None
            self.head = next_node

        self._length -= 1