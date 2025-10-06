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

    def pop_left(self) -> int:
        """
        Time complexity: O(1)
        Space Complexity: O(1)
        """
        rtr_value = self.head.value

        if self._length == 0:
            raise TypeError
        elif self._length == 1:
            self.head = self.tail = None
        else:
            next_node = self.head.next
            self.head.next = next_node.previous = None
            self.head = next_node

        self._length -= 1
        return rtr_value

    def pop_right(self) -> int:
        """
        Time complexity: O(1)
        Space Complexity: O(1)
        """
        rtr_val = self.tail.value

        if self._length == 0:
            raise TypeError
        elif self._length == 1:
            self.head = self.tail = None
        else:
            new_tail = self.tail.previous
            new_tail.next = self.tail.previous = None
            self.tail = new_tail

        self._length -= 1
        return rtr_val

    def remove(self, value: int) -> None:
        """
        Time complexity: O(n)
        Space Complexity: O(1)
        """
        if self._length == 0:
            raise TypeError

        # Iterate through the structure
        cur_node: Node = self.head
        while cur_node.value != value:
            if cur_node.next is None:
                return BaseException
            else:
                cur_node = cur_node.next

        # remove node
        if cur_node.next is not None: cur_node.next.previous = cur_node.previous
        if cur_node.previous is not None: cur_node.previous.next = cur_node.next

        # update length
        self._length -=1