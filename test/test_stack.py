from src.stack import Stack

def test_push_positive_1() -> None:
    """
    Positive test for push()
    """
    # Arrange
    stack = Stack()

    # Act
    for i in range(5):
        x = stack.push(i)

    # Assert
    assert isinstance(x, Stack)
    assert x._top.value == 4
    assert len(x) == 5

def test_pop_positive_1() -> None:
    """
    Positive test for pop()
    """
    # Arrange
    stack = Stack()
    for i in range(5):
        stack.push(i)

    # Act
    tmp_list = []
    for _ in range(3):
        tmp_list.append(stack.pop())

    # Assert
    assert tmp_list == [4,3,2]
    assert stack._top.value == 1
    assert len(stack) == 2

