from collections import deque

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
        todo revisit insert... how do I exactly have a node with 2 children?
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
            self.root = current.right if current.right else current.left
            return self

        elif parent.left is current:
            # the node is on the left of the parent
            parent.left = current.right if current.right else current.left

        elif parent.right is current:
            # the node is on the right of the parent
            parent.right = current.right if current.right else current.left

        return self

    def _remove_node_two_children(self, current: Node):
        successor = self._get_successor(current)
        current.value = successor.value
        return self.remove(successor.value, start=current.right, parent=current)

    @staticmethod
    def _get_successor(current: Node):
        # Step right...
        successor = current.right
        # Step all the way to the left! While there is a successor and there is a left child,
        # move to that left child :) :D :P xD
        while successor and successor.left:
            successor = successor.left
        return successor

    def bf_traversal(self) -> list[int]:
        """
        Time complexity:
        Space complexity:
        """
        if self.root is None: raise Exception()

        queue: deque[Node] = deque()
        visited: list[int] = []

        queue.append(self.root)
        while queue:
            selected = queue.popleft()
            if selected.left:
                queue.append(selected.left)
            if selected.right:
                queue.append(selected.right)

            visited.append(selected.value)

        return visited

    def df_pre_ord_traversal(self) -> list[int]:
        if self.root is None: raise Exception()

        stack: list[Node] = [self.root]
        visited: list[int] = []

        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.value)
            if visited_node.left:
                stack.append(visited_node.left)
            if visited_node.right:
                stack.append(visited_node.right)

        return visited

    def df_pre_ord_iterative(self) -> list[int]:
        if self.root is None:
            raise Exception()
        visited = []

        def _traverse(node: Node):
            if node:
                visited.append(node.value)
                _traverse(node.left)
                _traverse(node.right)
            return

        _traverse(self.root)
        return visited
