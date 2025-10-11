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

def test_remove_pos_1():
    # Arrange
    dll = DoubleLinkedList()
    for i in range(0,5):
        dll.append(i)

    # Act
    dll.remove(3)

    # Assert
    n = dll.head
    for i in [0,1,2,4]:
        assert n.value == i
        n = n.next

def test_remove_pos_2():
    # Arrange
    dll = DoubleLinkedList()
    for i in range(0,5):
        dll.append(i)

    # Act
    dll.remove(0)

    # Assert
    n = dll.head
    for i in [1,2,3,4]:
        assert n.value == i
        n = n.next

def test_remove_pos_3():
    # Arrange
    dll = DoubleLinkedList()
    for i in range(0,5):
        dll.append(i)

    # Act
    dll.remove(4)

    # Assert
    n = dll.head
    for i in [0,1,2,3]:
        assert n.value == i
        n = n.next

def test_remove_pos_4():
    # Arrange
    dll = DoubleLinkedList()
    dll.append(0)

    # Act
    dll.remove(0)

    # Assert
    assert dll.head is None
    assert dll.tail is None