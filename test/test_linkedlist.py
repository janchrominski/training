import pytest

from src.linkedlist import LinkedList, Node
from pytest import fixture

def __iterate_through_ll(ll: Node) -> list:
    """
    function which will return all the values from the ll
    """
    def recursion(node: Node, val_list: list = []) -> list:
        val_list.append(node.value)
        if node.next is not None:
            recursion(node.next)

        return val_list

    return recursion(ll.head)

@pytest.fixture
def basic_ll() -> LinkedList:
    ll_obj = LinkedList()

    for i in range(5):
        ll_obj.append(i)

    return ll_obj

def test_ll_append(basic_ll) -> None:
    """
    test the append method
    """
    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(5)]

def test_ll_prepend(basic_ll) -> None:
    """
    test the prepend method
    """
    ll = basic_ll
    ll.prepend(-1)

    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(-1,5)]

def test_ll_pop_left(basic_ll) -> None:
    """
    test the pop_left method
    """
    ll = basic_ll
    zero = ll.pop_left()

    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(1,5)]
    assert zero == 0

def test_ll_pop_right(basic_ll) -> None:
    """
    test the pop_right method
    """
    ll = basic_ll
    four = ll.pop_right()

    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(0, 4)]
    assert four == 4

def test_remove_1(basic_ll) -> None:
    """
    test remove first node
    """
    ll = basic_ll
    zero = ll.remove(0)

    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(1, 5)]
    assert zero == 0

def test_remove_2(basic_ll) -> None:
    """
    test remove middle node
    """
    ll = basic_ll
    three = ll.remove(3)

    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(0, 5) if x is not 3]
    assert three == 3

def test_remove_3(basic_ll) -> None:
    """
    test remove end node
    """
    ll = basic_ll
    four = ll.remove(4)

    list_of_vals = __iterate_through_ll(basic_ll)

    assert list_of_vals == [x for x in range(0, 4)]
    assert four == 4

def test_reverse(basic_ll) -> None:
    """
    test reverse
    """
    ll = basic_ll
    ll.reverse()

    list_of_vals = __iterate_through_ll(ll)

    assert list_of_vals == [x for x in range(4, -1, -1)]

    print('wow')
