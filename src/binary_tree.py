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

    def remove(self, value, start=None, parent=None):
        current = start or self.root
        while current and current.value != value:
            # Save parent
            parent = current
            # Get relevant child
            if value < current.value:
                current = parent.left
            else:
                current = parent.right

        # Process the child
        if not current:
            raise Exception("item not in tree")
        # We found a node and it has no children
        if not current.right and not current.left:
            return self._remove_node_no_children(current,parent)
        elif current.right and current.left:
            return self._remove_node_two_children(current)
        return self._remove_node_one_child(current, parent)

    def _remove_node_no_children(self, current: Node, parent: Node):
        if current is self.root:
            self.root = None
            return self
        if parent.left == current:
            parent.left = None
        elif parent.right == current:
            parent.right = None
        else:
            raise Exception()
        return self

    def _remove_node_one_child(self, current: Node, parent: Node):
        if current is self.root:
            self.root = None
            return self
        elif parent.left is current:
            # the node is on the left of the parent

            if current.left is not None and current.right is None:
                #the one child is on the left
                parent.left = current.left
            elif current.left is None and current.right is not None:
                #the one child is on the right
                parent.left = current.right
            else:
                raise Exception()

        elif parent.right is current:
            # the node is on the right of the parent

            if current.left is not None and current.right is None:
                #the one child is on the left
                parent.right = current.left
            elif current.left is None and current.right is not None:
                #the one child is on the right
                parent.right = current.right
            else:
                raise Exception()
        else:
            raise Exception()
        return self
