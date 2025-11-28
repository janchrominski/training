from src.binary_tree import BinarySearchTree, Node
import random

def is_valid_bst(node: Node,
                 min_val: float=float("-inf"),
                 max_val: float=float("inf")) -> bool:
    if node is None:
        return True
    if not (min_val < node.value < max_val):
        return False
    return (
        # Testing Right
        is_valid_bst(node=node.left,
                     min_val=min_val,
                     max_val=node.value) and
        # Testing Left
        is_valid_bst(node=node.right,
                     min_val=node.value,
                     max_val=max_val)
    )

def test_tree() -> None:
    # Arrange
    tree = BinarySearchTree()

    # Act
    for _ in range(20):
        tree.insert(random.randint(0,50))

    # Assert
    assert is_valid_bst(tree.root)

def test_binary_tree() -> None:
    # Arrange
    tree = BinarySearchTree()

    # Act
    for i in range(1,20+1):
        tree.insert(i)

    # Assert
    for i in range(1,20+1):
        assert tree.contains(i)

def test_tree_remove_1():
    # Arrange
    tree = BinarySearchTree()

    # Act
    for i in range(1,20+1):
        tree.insert(i)

    # Assert
    tree.remove(value=20)
    assert not tree.contains(20)
