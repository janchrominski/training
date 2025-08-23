class Node:
    next: object
    value: any

    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    head: Node = None
    tail: Node = None
    length: int = 0

    def append(self, value: int) -> None:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        new_node = Node(value=value)

        if self.length == 0:
            # establish head and tailas the new node
            self.head = self.tail = new_node
        else:
            # point to the new tail
            self.tail.next = new_node
            # establish the new tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value: int) -> None:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        new_node = Node(value=value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            # add the next relationship
            new_node.next = self.head
            # make the new head
            self.head = new_node

        self.length += 1

    def pop_left(self) -> int:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.length == 0:
            raise Exception()
        elif self.length == 1:
            self.head = self.tail = None
        else:
            # Get reference to the old head
            old_head = self.head
            # Establish the new head
            self.head = self.head.next
            # remove the old head
            old_head.next = None

        self.length -= 1

        return old_head.value

    def pop_right(self) -> int:
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        old_value = None
        if self.length == 0:
            raise Exception()
        elif self.length == 1:
            old_value = self.head
            self.head = self.tail = None
        elif self.length == 2:
            old_value = self.head.next
            self.head.next = None
            self.head = self.tail
        else:
            # iterate to find the last node
            tmp_node = self.head
            while tmp_node.next is not self.tail:
                tmp_node = tmp_node.next
            # Save the old value
            old_value = self.tail
            tmp_node.next = None
            self.tail = tmp_node

        self.length -= 1
        return old_value.value

    def remove(self, removee: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        old_value = int

        # check for no 0 length
        if not self.length:
            raise Exception("List is empty")
        # check for 1 length
        elif removee == self.head.value:
            old_value = self.head.value
            self.head = self.tail
        # check for 2 <= length
        current_node = self.head
        next_node = self.head.next
        ## check if next node is the removee
        while next_node.value != removee:
            current_node = current_node.next
            next_node = current_node.next
        ## preserve the old value to be returned
        old_value = next_node.value
        ## destroy next node but preserve node after that
        if next_node.next is not None:
            current_node.next = next_node.next
        else:
            current_node.next = None

        self.length -= 1
        return old_value
