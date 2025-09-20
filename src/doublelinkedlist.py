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
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self._length += 1