from src.queue import Queue, Node

def test_queue_enque() -> None:
    """
    Queue positive test 1
    """
    # Arrange
    queue = Queue()

    # Act
    # Assert
    for i in range(0,5):
        queue.enqueue(Node(i))

def test_queue_deque() -> None:
    """
    Queue positive test 1
    """
    # Arrange
    queue = Queue()
    for i in range(0,5):
        queue.enqueue(Node(i))

    # Act
    # Assert
    for i in range(4,-1):
        assert queue.dequeue() == i