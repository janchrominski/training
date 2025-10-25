from typing import Union

class Node:
    next: object
    value: int

    def __init__(self, value: int):
        self.value = value

class Stack:
    def __init__(self):
        self._top: Node = None
        self._size: int = 0
        self._max_allowed_size: int = 100

    def __len__(self) -> int:
        return self._size

    def push(self, value: int) -> object:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self._size == self._max_allowed_size:
            raise Exception("Max Allowed Size Exceeded!")
        new_node: Node = Node(value)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        return self

    def pop(self) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._size:
            raise Exception("Stack is empty")
        former_top = self._top
        self._top = self._top.next
        former_top.next = None
        self._size -= 1
        return former_top.value

    def peek(self) -> Union[int,None]:
        return self._top.value if self._top else None

    def clear(self) -> object:
        self._top = None
        self._size = 0
        return self