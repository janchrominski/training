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
    # Remove a leaf node with no children

    # Arrange
    tree = BinarySearchTree()

    # Act
    for i in range(1,20+1):
        tree.insert(i)

    # Assert
    tree.remove(value=20)
    assert not tree.contains(20)

def test_tree_remove_2():
    # Remove a leaf node with a child

    # Arrange
    tree = BinarySearchTree()

    # Act
    for i in (5,4,3):
        tree.insert(i)

    # Assert
    tree.remove(value=4)
    assert not tree.contains(4)
    assert tree.root.value == 5
    assert tree.root.left.value == 3

def test_tree_remove_3():
    # Remove a leaf node with two children!!!

    # Arrange
    tree = BinarySearchTree()
    for i in (10, 5, 15, 12, 18):
        tree.insert(i)

    # Act
    tree.remove(10)

    # Assert
    assert tree.root.value == 12
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15
    assert tree.root.right.right.value == 18
    assert tree.root.right.left is None

def test_bf_traversal():
    # Arrange
    # Initiate and fill the tree
    tree = BinarySearchTree()
    tree_tuple = (10, 5, 15, 12, 18)
    for i in tree_tuple:
        tree.insert(i)

    # Act
    result_list: list[int] = tree.bf_traversal()

    # Assert
    assert len(result_list) == len(tree_tuple)

    for i in range(len(tree_tuple)):
        assert result_list[i] == tree_tuple[i]

def test_df_pre_ord_traversal():
    # Arrange
    # Initiate and fill the tree
    tree: BinarySearchTree = BinarySearchTree()
    tree_tuple: tuple[int] = (10, 5, 15, 12, 18)
    for i in tree_tuple:
        tree.insert(i)

    # Act
    a: list[int] = tree.df_pre_ord_traversal()
    b: list[int] = tree.bf_traversal()

    # Assert
    assert_tree_tuple: tuple[int] = (10,15,18,12,5)
    assert len(a) == len(b) == len(tree_tuple)


    for i in range(len(assert_tree_tuple)):
        assert assert_tree_tuple[i] in a and assert_tree_tuple[i] in b

def test_df_pre_ord_iterative():
    # Arrange
    # Initiate and fill the tree
    tree: BinarySearchTree = BinarySearchTree()
    tree_tuple: tuple[int] = (10, 5, 15, 12, 18)
    for i in tree_tuple:
        tree.insert(i)

    # Act
    a: list[int] = tree.df_pre_ord_iterative()
    b: list[int] = tree.bf_traversal()

    # Assert
    assert_tree_tuple: tuple[int] = (10, 15, 18, 12, 5)
    assert len(a) == len(b) == len(tree_tuple)

    for i in range(len(assert_tree_tuple)):
        assert assert_tree_tuple[i] in a and assert_tree_tuple[i] in b

def test_df_in_ord_iterative():
    # Arrange
    # Initiate and fill the tree
    tree: BinarySearchTree = BinarySearchTree()
    tree_tuple: tuple[int] = (10, 5, 15, 12, 18)
    for i in tree_tuple:
        tree.insert(i)

    # Act
    a: list[int] = tree.df_in_ord_traversal()
    b: list[int] = [5,10,12,15,18]

    # Assert
    for i in range(len(tree_tuple)):
        assert a[i].value == b[i]

def test_df_in_ord_recursion():
    # Arrange
    # Initiate and fill the tree
    tree: BinarySearchTree = BinarySearchTree()
    tree_tuple: tuple[int] = (10, 5, 15, 12, 18)
    for i in tree_tuple:
        tree.insert(i)

    # Act
    a: list[int] = tree.df_in_ord_recursion()
    b: list[int] = [5,10,12,15,18]

    # Assert
    for i in range(len(tree_tuple)):
        assert a[i] == b[i]

def test_df_post_order_iterative():
    # Arrange
    # Initiate and fill the tree
    tree: BinarySearchTree = BinarySearchTree()
    tree_tuple: tuple[int] = (10, 5, 15, 12, 18)
    for i in tree_tuple:
        tree.insert(i)

    # Act
    a: list[int] = tree.df_post_ord_traversal()
    b: list[int] = [5, 12, 18, 15, 10]

    # Assert
    for i in range(len(tree_tuple)):
        assert a[i] == b[i]