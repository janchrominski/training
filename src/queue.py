from beartype import beartype

class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: object = None

class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    @beartype
    def enqueue(self, new_node: Node) -> None:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.size == 0:
            self.tail = self.head = new_node
        elif self.size > 1:
            new_node.next = self.tail
            self.tail = new_node

        self.size += 1

    @beartype
    def dequeue(self) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self.size == 0:
            raise Exception
        elif self.size == 1:
            self.tail = self.head = None
        else:
            # iterate through the queue
            a = self.tail
            b = None
            while a.next is not None:
                b = a
                a = a.next
            b.next = None
            self.head = b

        self.size -= 1