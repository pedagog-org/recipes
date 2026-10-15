import pytest
from pedagog_pytest import number, solution_expect, visibility, weight

from linked_list import LinkedList


@weight(2)
@number(1)
def test_append_and_to_list():
    """append keeps insertion order"""
    items = LinkedList()
    for value in [3, 1, 4]:
        items.append(value)
    assert items.to_list() == [3, 1, 4]


@weight(2)
@number(2)
def test_len():
    """len counts elements"""
    items = LinkedList()
    assert len(items) == 0
    items.append("x")
    items.append("y")
    assert len(items) == 2


@weight(3)
@number(3)
@visibility(output="hidden")
def test_pop_front():
    """pop_front removes from the front and raises when empty"""
    items = LinkedList()
    items.append(1)
    items.append(2)
    assert items.pop_front() == 1
    assert items.to_list() == [2]
    assert items.pop_front() == 2
    with pytest.raises(IndexError):
        items.pop_front()


@weight(1)
@number(4)
@solution_expect("fail")
def test_reverse_stretch_goal():
    """stretch goal: reverse() (the reference solution doesn't implement it)"""
    items = LinkedList()
    items.append(1)
    items.append(2)
    items.reverse()
    assert items.to_list() == [2, 1]
