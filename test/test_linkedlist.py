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

