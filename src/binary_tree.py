class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value: int) -> None:
        """
        O complexity space: O(1)
        O complexity time: O(log n)
        """
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        # Start of tree traversal
        current_node = self.root

        while value != current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node

                # Proceed to the next level
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node

                # Proceed to the next level
                current_node = current_node.right

    def contains(self, value: int) -> bool:
        """
        O complexity space: O(1)
        O complexity time: O(n) best and 0(log n) worst
        """
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False