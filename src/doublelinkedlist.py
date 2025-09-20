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
        new_node = Node(value=new_val, next=self.head)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
        elif self._length == 1:
            self.head = new_node
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

        self._length += 1