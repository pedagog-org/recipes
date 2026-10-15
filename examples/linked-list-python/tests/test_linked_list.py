import pytest
from pedagog_pytest import (
    HIDDEN, Expect, Rubric, Score, item, number, rubric, rubric_item, solution_expect, visibility, weight,
)

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


class PopFront(Rubric):
    returns_front: Score = item("returns values from the front", points=2)
    raises_when_empty: Score = item("raises IndexError when empty", points=1)
    reusable: Score = item("the list still works after being emptied", points=1, extra_credit=True)


@rubric(PopFront)
@number(3)
@visibility(output=HIDDEN)
def test_pop_front(scores: PopFront):
    """pop_front"""
    items = LinkedList()
    items.append(1)
    items.append(2)
    with scores.returns_front.check():
        assert items.pop_front() == 1
        assert items.pop_front() == 2
    with scores.raises_when_empty.check():
        with pytest.raises(IndexError):
            items.pop_front()
    with scores.reusable.check():
        items.append(3)
        assert items.to_list() == [3]


@weight(1)
@number(4)
@solution_expect(Expect.FAIL)
def test_reverse_stretch_goal():
    """stretch goal: reverse() (the reference solution doesn't implement it)"""
    items = LinkedList()
    items.append(1)
    items.append(2)
    items.reverse()
    assert items.to_list() == [2, 1]


@rubric_item("handles a thousand elements", points=2)
@number(5)
def test_many_elements(score: Score):
    """Half credit if the first elements are right, full credit if all are."""
    items = LinkedList()
    for value in range(1000):
        items.append(value)
    result = items.to_list()
    if result[:10] == list(range(10)):
        score.award(1)
    assert result == list(range(1000))
    score.award()
