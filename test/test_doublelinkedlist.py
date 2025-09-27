from ..src.doublelinkedlist import DoubleLinkedList

def test_append_pos_1():
    # Arrange
    dll = DoubleLinkedList()

    # Act
    for i in range(0,5):
        dll.append(i)

    # Assert going forward
    n = dll.head
    for i in range(0,5):
        assert n.value == i
        n = n.next

    # Assert going backward
    n = dll.tail
    for i in range(5,0):
        assert n.value == i
        n = n.previous

def test_prepend_pos_1():
    # Arrange
    dll = DoubleLinkedList()

    # Act
    for i in range(0,5):
        dll.prepend(i)

    # Assert
    n = dll.head
    for i in range(5,0):
        assert n.value == i
        n = n.next

def test_pop_left_pos_1():
    # Arrange
    dll = DoubleLinkedList()

    # Act
    for i in range(0,5):
        dll.prepend(i)
    ass_val = dll.pop_left()

    # Assert
    assert ass_val == 4

def test_pop_right_pos_1():
    # Arrange
    dll = DoubleLinkedList()

    # Act
    for i in range(0,5):
        dll.prepend(i)
    ass_val = dll.pop_right()

    # Assert
    assert ass_val == 0